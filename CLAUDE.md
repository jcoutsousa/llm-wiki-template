# LLM Wiki Schema: AI and Innovation

This document configures the LLM to maintain a personal knowledge base on **AI and Innovation**, ingesting research papers and books.

## Directory Structure

```
/
├── raw/              # Immutable source documents
│   ├── papers/       # Research papers (PDF, Markdown)
│   └── books/        # Book excerpts, notes (PDF, Markdown, TXT)
├── wiki/
│   ├── entities/     # People, organizations, models, technologies
│   ├── concepts/     # Techniques, frameworks, methodologies
│   ├── sources/      # Summaries and analysis of each source
│   ├── comparisons/  # Model comparisons, method comparisons
│   └── index.md      # Catalog of all wiki pages
└── log.md            # Chronological record of all operations
```

## Page Conventions

### Entity Pages (`wiki/entities/`)
- One entity per file: `gpt-4.md`, `openai.md`, `transformer.md`
- Frontmatter: `aliases`, `related`, `first_seen`, `last_updated`
- Sections: Overview, Key Contributions, Impact, References

### Concept Pages (`wiki/concepts/`)
- One concept per file: `attention.md`, `rlhf.md`, `diffusion-models.md`
- Frontmatter: `category`, `related_concepts`, `sources_count`
- Sections: Definition, History, Applications, References

### Source Summaries (`wiki/sources/`)
- Filename: sanitized source title, e.g., `attention-is-all-you-need.md`
- Frontmatter: `authors`, `year`, `venue`, `tags`, `key_entities`, `key_concepts`
- Executive Summary, Key Findings, Methodology (for papers), Impact, Wiki Updates
- Cross-references to entities/concepts already updated

## Workflows

### Ingest Workflow
1. User drops source into `raw/papers/` or `raw/books/`
2. LLM reads source, discusses key takeaways with user
3. LLM creates/updates relevant entity and concept pages
4. LLM creates source summary page in `wiki/sources/`
5. LLM updates `wiki/index.md` with new/modified pages
6. LLM appends entry to `log.md` with format: `## [YYYY-MM-DD] ingest | Source Title`

### Query Workflow
1. Read `wiki/index.md` to find relevant pages
2. Read relevant pages, synthesize answer with citations
3. If answer has lasting value, create new page in appropriate category
4. Append query and new page to `log.md`

### Lint Workflow
1. Check for contradictions between pages
2. Find stale claims superseded by newer sources
3. Identify orphan pages (no inbound links)
4. Find concepts/entities mentioned but lacking their own page
5. Suggest new sources to investigate

## Index Format

`wiki/index.md` entries follow:
- `[entities/]` - Person, organization, model, technology pages
- `[concepts/]` - Technique, framework, methodology pages
- `[sources/]` - Source summary pages

Each entry: `[Title](path/to/file.md) | one-line summary | N sources | YYYY-MM-DD`

## Source Handling

- Research papers: Extract methodology, results, implications; link to arXiv/DOI
- Books: Extract key chapters, arguments, frameworks; cite edition and page numbers
- All sources immutable; only wiki pages change