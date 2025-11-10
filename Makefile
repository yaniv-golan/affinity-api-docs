.PHONY: sync-v1 link-check qa test

sync-v1:
	python tools/v1_sync_pipeline/sync_v1_docs.py $(ARGS)

link-check:
	python tools/v1_sync_pipeline/qa/check_links.py docs/v1/affinity_api_docs.md

qa: sync-v1 link-check

test:
	pytest tests/ -m "not integration" -v
