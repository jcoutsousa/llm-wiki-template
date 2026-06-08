.PHONY: update-wiki clean-wiki

update-wiki:
	python3 scripts/wiki_sync.py --once

clean-wiki:
	python3 scripts/wiki_ingest_dedup.py --yes --rebuild-index
