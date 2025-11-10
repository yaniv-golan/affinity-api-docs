# Auto-Sync Rollout Lessons (2025-11-10)

## Highlights

- Promoted `tools/v1_sync_pipeline/sync_v1_docs.py` as the only supported ingestion path; QA scripts now ship alongside it.
- Daily workflow now runs the sync script with `--fail-on-diff`, executes link checks, and opens PRs via `peter-evans/create-pull-request`.
- Tests workflow blocks manual edits by running the sync pipeline during CI and running pytest against parser utilities.

## Action Items

1. Monitor the first scheduled `Sync Affinity v1 Docs` run to confirm PR creation and link-check output.
2. Keep `tmp/` artifacts reviewed locally only; never commit them.
3. When Affinity fixes in-page anchors, trim `BROKEN_ANCHOR_MAP` and update the quarterly issue template.
