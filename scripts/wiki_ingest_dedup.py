#!/usr/bin/env python3
"""
wiki_ingest_dedup.py — Remove duplicatas de wiki/sources/ baseadas no stem do arquivo.
Prefere .md sobre .pdf e nomes curtos (<255) sobre inteiros com timestamp.

Uso:
  python3 wiki_ingest_dedup.py              # Dry run (mostra duplicatas)
  python3 wiki_ingest_dedup.py --yes        # Remove de fato
  python3 wiki_ingest_dedup.py --yes --rebuild-index
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

REPO_ROOT = Path(__file__).parent.parent
WIKI_SOURCES = REPO_ROOT / "wiki" / "sources"
WIKI_INDEX = REPO_ROOT / "wiki" / "index.md"

YES = "--yes" in sys.argv
REBUILD_INDEX = "--rebuild-index" in sys.argv
DRY_RUN = not YES


def stem_key(filename: str) -> str:
    stem = filename.replace(".md", "").replace(".pdf", "")
    stem = re.sub(r"_\d{9,}$", "", stem)
    return stem.lower().replace("_", "-").replace(" ", "-")


def is_short(name: str) -> bool:
    return len(name) < 255


def find_duplicates() -> dict:
    groups = defaultdict(list)
    if not WIKI_SOURCES.exists():
        return groups
    for f in sorted(WIKI_SOURCES.glob("*.md")):
        groups[stem_key(f.name)].append(f)
    return {k: v for k, v in groups.items() if len(v) > 1}


def choose_canonical(files: list) -> Path:
    """Prefere .md, depois nome curto, depois alfabético."""
    return sorted(files, key=lambda p: (
        0 if p.suffix == ".md" else 1,
        0 if is_short(p.name) else 1,
        p.name,
    ))[0]


def main():
    dups = find_duplicates()
    if not dups:
        print("✅ Nenhuma duplicata encontrada.")
        return

    print(f"🔍 Encontrados {len(dups)} grupos de duplicatas ({sum(len(v) for v in dups.values())} arquivos):\n")
    to_remove = []
    for stem, files in sorted(dups.items()):
        canonical = choose_canonical(files)
        print(f"  [{stem}]")
        for f in files:
            tag = " ✓ CANÔNICO" if f == canonical else " ✗ REMOVER"
            print(f"    {f.name}{tag}")
            if f != canonical:
                to_remove.append(f)
        print()

    if DRY_RUN:
        print("— Rodar com --yes para remover as duplicatas marcadas —")
        return

    removed = 0
    for f in to_remove:
        print(f"  🗑️  Removendo {f.name}")
        f.unlink()
        removed += 1

    print(f"\n✅ Removidas {removed} duplicatas.")

    if REBUILD_INDEX:
        print("🔄 Reconstruindo wiki/index.md...")
        regenerate_index()
        print("✅ Index atualizado.")


def regenerate_index():
    hoje = datetime.now().strftime("%Y-%m-%d")
    lines = [
        "# LLM Wiki Index\n\n",
        "## [entities/] - Person, organization, model, technology pages\n\n",
        "_(Gerado automaticamente — edite manualmente ou use agentes para popular)_\n\n",
        "## [concepts/] - Technique, framework, methodology pages\n\n",
        "_(Gerado automaticamente — edite manualmente ou use agentes para popular)_\n\n",
        "## [sources/] - Source summary pages\n\n",
    ]

    if WIKI_SOURCES.exists():
        sources = sorted(WIKI_SOURCES.glob("*.md"))
        if sources:
            for src in sources:
                try:
                    title = src.stem.replace("_", " ").replace("-", " ").title()
                    lines.append(f"- [{title}](sources/{src.name})\n")
                except Exception:
                    continue
        else:
            lines.append("_(Nenhuma fonte sincronizada ainda)_\n")
    else:
        lines.append("_(Nenhuma fonte sincronizada ainda)_\n")

    WIKI_INDEX.write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
