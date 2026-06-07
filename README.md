# LLM Wiki Template

A template for building personal knowledge bases using LLMs, based on Andrej Karpathy's LLM Wiki pattern.

## Structure

```
/
├── raw/              # Immutable source documents
│   ├── papers/       # Research papers (PDF)
│   └── books/        # Book excerpts
├── wiki/
│   ├── entities/     # People, organizations, models
│   ├── concepts/     # Techniques, frameworks
│   ├── sources/      # Source summaries
│   └── index.md      # Catalog
└── log.md            # Operations log
```

## Setup

### For Kilo Projects

1. Copy `.agents/skills/setup-llm-wiki/` to `~/.agents/skills/` (or use `.kilo/agent/AGENTS.md` in project)
2. Add path to `kilo.jsonc` external_directory permissions

### For Claude Code / OpenCode

1. Rename `.agents/skills/setup-llm-wiki/AGENTS.md` to `CLAUDE.md` in your project
2. Modify for your domain

### General Workflow
1. Determine topic and source types (papers, books, articles, etc.)
2. Create directory structure
3. Write schema file
4. Create initial index.md and log.md
5. Drop sources into `raw/` subdirectories
6. Ingest sources to build wiki

## Ingest Workflow

1. Extract text from PDFs: `pdftotext`
2. Create source summary in `wiki/sources/`
3. Update/create entity/concept pages
4. Update `wiki/index.md` and `log.md`

## Included Skill Files

- `.agents/skills/SKILL.md` - Kilo skill format
- `.agents/skills/AGENTS.md` - Universal agent format
- `.agents/skills/README.md` - Standalone documentation
- `.kilo/agent/AGENTS.md` - Project-level loading for Kilo

## Note

`.gitignore` excludes `raw/papers/*.md` (extracted text regenerated from PDFs)