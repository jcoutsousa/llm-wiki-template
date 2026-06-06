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

1. Copy `.agents/skills/setup-llm-wiki/` to your agent's skills directory (e.g., `~/.agents/skills/`)
2. Modify `CLAUDE.md` to match your domain
3. Drop sources into `raw/papers/` or `raw/books/`
4. Ingest sources to build your wiki

## Ingest Workflow

1. Extract text from PDFs: `pdftotext`
2. Create source summary in `wiki/sources/`
3. Update/create entity/concept pages
4. Update `wiki/index.md` and `log.md`