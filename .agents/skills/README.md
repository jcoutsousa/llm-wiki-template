# Setup LLM Wiki

Platform-agnostic instructions for initializing LLM-powered knowledge bases.

## Quick Start

1. Determine topic/domain and source types (papers, books, articles, etc.)
2. Create directory structure (see below)
3. Write schema file for your editor
4. Create initial index.md and log.md

## Directory Structure

```
/
├── raw/              # Immutable source documents
├── wiki/
│   ├── entities/     # People, organizations, models, technologies
│   ├── concepts/     # Techniques, frameworks, methodologies
│   ├── sources/      # Summaries of each source
│   └── index.md      # Catalog
└── log.md            # Chronological record
```

## Workflows

- **Initialize**: Create dirs, write schema, create templates
- **Ingest**: Extract text → analyze → create wiki pages → update logs