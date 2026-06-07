---
name: setup-llm-wiki
description: "Initialize and configure LLM-powered knowledge bases with directory structure, schema, and ingestion workflows. Platform-agnostic for any coding assistant. WHEN: set up wiki, personal knowledge base, LLM wiki, knowledge management system."
license: MIT
---

# Setup LLM Wiki

Configure an LLM Wiki by providing the topic and source types, then create the directory structure and schema file.

## Directory Structure

```
/
├── raw/              # Immutable source documents
│   ├── papers/       # Research papers (if applicable)
│   ├── books/        # Book excerpts (if applicable)
│   └── articles/     # Web articles (if applicable)
├── wiki/
│   ├── entities/     # People, organizations, models, technologies
│   ├── concepts/     # Techniques, frameworks, methodologies
│   ├── sources/      # Summaries and analysis of each source
│   ├── comparisons/  # Model/method comparisons
│   └── index.md      # Catalog of all wiki pages
└── log.md            # Chronological record of operations
```

## Workflows

### Initialize Wiki Repository

1. Ask user: What topic/domain? What source types? (research papers, books, articles, websites, videos, podcasts, tweets, etc.)
2. Create directory structure based on source types:
   - Always create `raw/` base directory
   - `raw/papers/` for research papers (if papers)
   - `raw/books/` for book excerpts (if books)
   - `raw/articles/` for web articles (if articles)
   - Add other subdirectories as needed
3. Create standard wiki subdirectories: wiki/entities/, wiki/concepts/, wiki/sources/, wiki/comparisons/
4. Write platform-specific schema file (AGENTS.md for this environment)
5. Create initial wiki/index.md and log.md
6. Document page conventions for the specific domain

### Ingest Sources

1. Extract text from sources:
   - PDFs: pdftotext
   - Other formats: appropriate tool (pandoc, yt-dlp, etc.)
2. Read source content
3. Identify key entities and concepts
4. Create/update corresponding wiki pages
5. Write source summary with frontmatter
6. Update index.md and log.md

## Directory Structure

```
/
├── raw/              # Immutable source documents
│   ├── papers/       # Research papers (if applicable)
│   ├── books/        # Book excerpts (if applicable)
│   └── articles/     # Web articles (if applicable)
├── wiki/
│   ├── entities/     # People, organizations, models, technologies
│   ├── concepts/     # Techniques, frameworks, methodologies
│   ├── sources/      # Summaries and analysis of each source
│   ├── comparisons/  # Model/method comparisons
│   └── index.md      # Catalog of all wiki pages
└── log.md            # Chronological record of operations
```

## Workflows

### Initialize Wiki Repository

1. Ask user: What topic/domain? What source types? (research papers, books, articles, websites, videos, podcasts, tweets, etc.)
2. Create directory structure based on source types:
   - Always create `raw/` base directory
   - `raw/papers/` for research papers (if papers)
   - `raw/books/` for book excerpts (if books)
   - `raw/articles/` for web articles (if articles)
   - Add other subdirectories as needed
3. Create standard wiki subdirectories: wiki/entities/, wiki/concepts/, wiki/sources/, wiki/comparisons/
4. Write platform-specific schema file (AGENTS.md for this environment)
5. Create initial wiki/index.md and log.md
6. Document page conventions for the specific domain

### Ingest Sources

1. Extract text from sources:
   - PDFs: pdftotext
   - Other formats: appropriate tool (pandoc, yt-dlp, etc.)
2. Read source content
3. Identify key entities and concepts
4. Create/update corresponding wiki pages
5. Write source summary with frontmatter
6. Update index.md and log.md