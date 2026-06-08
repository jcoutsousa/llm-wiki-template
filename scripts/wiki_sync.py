#!/usr/bin/env python3
"""
wiki_sync.py — Monitora raw/papers/ e raw/books/ e atualiza a wiki automaticamente.
Uso:
  python3 wiki_sync.py [--once]   # Roda uma vez e sai
  python3 wiki_sync.py             # Roda em loop infinito (polling a cada 60s)
"""

import os
import re
import sys
import time
import shutil
from pathlib import Path
from datetime import datetime

try:
    import yaml
except ImportError:
    yaml = None

REPO_ROOT = Path(__file__).parent.parent
RAW_PAPERS = REPO_ROOT / "raw" / "papers"
RAW_BOOKS = REPO_ROOT / "raw" / "books"
WIKI_SOURCES = REPO_ROOT / "wiki" / "sources"
WIKI_ENTITIES = REPO_ROOT / "wiki" / "entities"
WIKI_CONCEPTS = REPO_ROOT / "wiki" / "concepts"
WIKI_INDEX = REPO_ROOT / "wiki" / "index.md"
LOG_FILE = REPO_ROOT / "log.md"
STATE_FILE = REPO_ROOT / ".wiki_sync_state.json"
POLL_INTERVAL = 60  # segundos

KNOWN_EXTENSIONS = {".md", ".pdf"}

def stem_key(file_path: Path) -> str:
    """Cluster .md/.pdf do mesmo documento pelo stem (sem timestamp)."""
    stem = file_path.stem
    # Remove timestamps tipo _1234567890
    stem = re.sub(r"_\d{9,}$", "", stem)
    # Normaliza bare name (ex: llm vs LLM)
    return stem.lower().replace(" ", "-").replace("_", "-")

# Title sanitization
def slugify_title(name: str) -> str:
    name = re.sub(r"[^\w\s-]", "", name, flags=re.UNICODE)
    name = re.sub(r"\s+", "-", name.strip())
    name = re.sub(r"-{2,}", "-", name)
    return name.lower().strip("-")


def today_str():
    return datetime.now().strftime("%Y-%m-%d")


def load_state():
    if STATE_FILE.exists():
        import json
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"synced": {}}


def save_state(state):
    import json
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def extract_pdf_text(pdf_path: Path) -> str:
    """Tenta extrair texto de PDF usando pdftotext."""
    try:
        import subprocess
        result = subprocess.run(
            ["/opt/homebrew/bin/pdftotext", str(pdf_path), "-"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            text = result.stdout.strip()
            if len(text) > 200:
                return text[:1500] + "…"
        return ""
    except Exception:
        return ""


def extract_md_info(md_path: Path) -> dict:
    """Lê frontmatter YAML e primeiras linhas do markdown."""
    info = {"title": md_path.stem, "authors": [], "year": "", "tags": [], "summary": ""}
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Tenta extrair frontmatter YAML
        if yaml is None:
            try:
                import yaml as _yaml
                fm_match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
                if fm_match:
                    fm = _yaml.safe_load(fm_match.group(1)) or {}
                    for k in ("title", "authors", "year", "tags", "venue"):
                        if k in fm:
                            info[k if k != "title" else "title"] = fm[k]
                    body = fm_match.group(2).strip()
                    info["summary"] = body[:300].replace("\n", " ") + "…" if len(body) > 300 else body
            except Exception:
                pass
        else:
            fm_match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
            if fm_match:
                fm = yaml.safe_load(fm_match.group(1)) or {}
                for k in ("title", "authors", "year", "tags", "venue"):
                    if k in fm:
                        info[k if k != "title" else "title"] = fm[k]
                body = fm_match.group(2).strip()
                info["summary"] = body[:300].replace("\n", " ") + "…" if len(body) > 300 else body

        if not info.get("title") or info["title"] == md_path.stem:
            # Tenta pegar primeiro H1
            h1 = re.search(r"^# (.+)", content, re.MULTILINE)
            if h1:
                info["title"] = h1.group(1).strip()
    except Exception as e:
        print(f"  [warn] Erro lendo {md_path}: {e}")
    return info


def extract_info(file_path: Path) -> dict:
    """Extrai metadados de um arquivo raw."""
    info = {"title": file_path.stem, "authors": [], "year": "", "tags": [],
            "summary": "", "venue": "", "file": file_path.name}

    if file_path.suffix == ".md":
        info.update(extract_md_info(file_path))
    elif file_path.suffix == ".pdf":
        text = extract_pdf_text(file_path)
        info["summary"] = text or "(PDF sem texto extraível)"
        # Tenta inferir título do nome sanitizado
        title = file_path.stem
        # Remove timestamps do final (ex: _1674728427)
        title = re.sub(r"_\d{9,}$", "", title)
        title = title.replace("_", " ").replace("-", " ").strip()
        info["title"] = title or file_path.stem

    return info


def create_source_page(info: dict, category: str) -> Path:
    """Cria/atualiza página em wiki/sources/."""
    slug = slugify_title(info["title"])
    dest = WIKI_SOURCES / f"{slug}.md"
    today = today_str()

    authors_str = ", ".join(info["authors"]) if isinstance(info["authors"], list) else str(info["authors"])
    tags_str = ", ".join(info["tags"]) if isinstance(info["tags"], list) else str(info["tags"])
    summary = info.get("summary", "(sem resumo)")

    content = f"""---
title: {info['title']}
authors: {authors_str}
year: {info.get('year', '')}
venue: {info.get('venue', '')}
tags: [{tags_str}]
category: {category}
key_entities: []
key_concepts: []
first_seen: {today}
last_updated: {today}
---

# {info['title']}

## Executive Summary

{summary}

## Key Findings

_(A ser preenchido durante ingestão manual ou automática com LLM)_

## Impact

_(A ser preenchido)_

## References

- Raw: [../raw/{category}/{info['file']}](../raw/{category}/{info['file']})
- First synced: {today}
"""

    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(content)
    return dest


def update_index(new_sources: list, removed_sources: list = None):
    """Reconstrói a seção [sources/] do index.md, deduplicando nome visual."""
    if removed_sources is None:
        removed_sources = []

    all_sources = []
    if WIKI_SOURCES.exists():
        for f in sorted(WIKI_SOURCES.glob("*.md")):
            if f.name == ".DS_Store":
                continue
            try:
                with open(f, "r", encoding="utf-8") as fh:
                    content = fh.read()
                fm = {}
                m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
                if m:
                    for line in m.group(1).splitlines():
                        if ":" in line:
                            k, v = line.split(":", 1)
                            fm[k.strip()] = v.strip().strip('"')
                title = fm.get("title", f.stem)
                year = fm.get("year", "")
                updated = fm.get("last_updated", fm.get("first_seen", ""))
                all_sources.append((title, f"sources/{f.name}", year, updated))
            except Exception:
                pass

    # Deduplica por stem normalizado
    seen = {}
    deduped = []
    for item in all_sources:
        title, path, year, updated = item
        norm = stem_key(path.split("/")[-1])
        if norm not in seen:
            seen[norm] = item
            deduped.append(item)

    today = today_str()
    lines = []
    lines.append("# LLM Wiki Index\n")
    lines.append("## [entities/] - Person, organization, model, technology pages\n")
    lines.append("_(Gerado automaticamente — edite manualmente ou use agentes para popular)_\n")

    lines.append("\n## [concepts/] - Technique, framework, methodology pages\n")
    lines.append("_(Gerado automaticamente — edite manualmente ou use agentes para popular)_\n")

    lines.append("\n## [sources/] - Source summary pages\n")
    if deduped:
        for (title, path, year, updated) in sorted(deduped, key=lambda x: x[0].lower()):
            year_info = f" | {year}" if year else ""
            date_info = f" | {updated}" if updated else ""
            lines.append(f"- [{title}]({path}){year_info}{date_info}\n")
    else:
        lines.append("_(Nenhuma fonte sincronizada ainda)_\n")

    with open(WIKI_INDEX, "w", encoding="utf-8") as f:
        f.writelines(lines)


def add_log_entry(title: str, category: str):
    today = today_str()
    entry = f"## [{today}] sync | {title}\nCategory: {category}\n\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)


def scan_directory(dir_path: Path, category: str) -> list:
    """Escaneia um diretório e retorna arquivos novos ou modificados, deduplicando por stem."""
    if not dir_path.exists():
        return []

    state = load_state()
    new_files = []
    seen = {}  # stem_key -> Path (prefere .md)

    for f in sorted(dir_path.glob("*")):
        if f.is_file() and f.suffix.lower() in KNOWN_EXTENSIONS:
            key = f"{category}:{f.name}"
            mtime = f.stat().st_mtime
            k = stem_key(f)
            if k not in seen or (f.suffix == ".md" and seen[k].suffix != ".md"):
                seen[k] = f
            if state["synced"].get(key) != mtime:
                # Marca como candidato; dedup final decide
                pass

    for f in seen.values():
        key = f"{category}:{f.name}"
        mtime = f.stat().st_mtime
        if state["synced"].get(key) != mtime:
            new_files.append(f)
            state["synced"][key] = mtime

    save_state(state)
    return new_files


def process_files(files: list, category: str):
    if not files:
        return 0
    count = 0
    print(f"\n📥 Processando {len(files)} arquivo(s) de {category}/...")
    for f in files:
        print(f"  → {f.name}")
        info = extract_info(f)
        if not info["title"]:
            print(f"    [warn] Sem título detectado, usando nome do arquivo")
        dest = create_source_page(info, category)
        add_log_entry(info["title"], category)
        print(f"    ✓ Criado {dest.name}")
        count += 1
    update_index([])
    print(f"✅ Sincronizados {count} fonte(s). Index atualizado.")
    return count


def sync_once():
    print("🔄 Wiki Sync — execução única\n")
    papers = scan_directory(RAW_PAPERS, "papers")
    books = scan_directory(RAW_BOOKS, "books")
    total = process_files(papers, "papers") + process_files(books, "books")
    if total == 0:
        print("✓ Nada de novo para sincronizar.")
    return total


def sync_loop():
    print(f"👁️  Wiki Sync — monitorando (polling a cada {POLL_INTERVAL}s)\n")
    print(f"  📂 {RAW_PAPERS}")
    print(f"  📂 {RAW_BOOKS}")
    print("  Pressione Ctrl+C para parar\n")
    try:
        while True:
            sync_once()
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print("\n\n🛑 Monitoramento parado.")


if __name__ == "__main__":
    if "--once" in sys.argv:
        sync_once()
    else:
        sync_loop()
