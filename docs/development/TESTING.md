# Testing the Affinity Docs Sync Pipeline

This guide explains how to exercise the production sync tooling (`tools/v1_sync_pipeline`) and the GitHub Actions workflows that keep `docs/v1/affinity_api_docs.md` up to date.

## Prerequisites

1. Python 3.11+
2. `pip install -r requirements-ci.txt`
3. Network access to https://api-docs.affinity.co/

> **Reminder:** Never edit `docs/v1/affinity_api_docs.md` by hand. Regenerate via the sync script.

## Core Test Flow

### 1. Run the Sync Script (idempotency check)

```bash
python tools/v1_sync_pipeline/sync_v1_docs.py --fail-on-diff
```

- Exit code `0`: no diff detected.
- Exit code `1`: markdown changed; rerun without `--fail-on-diff` if you just need the updated file for local inspection.
- Output files:
  - `docs/v1/affinity_api_docs.md` (canonical doc)
  - `tmp/snapshots/` (HTML snapshots, gitignored)
  - `tmp/code_blocks_sync.json`, `tmp/v1_sync_metadata.json`

### 2. Run the Link Checker

```bash
python tools/v1_sync_pipeline/qa/check_links.py docs/v1/affinity_api_docs.md
```

Confirms all internal anchors resolve and external links respond (with retries via GET if HEAD fails).

### 3. Run Pytest

```bash
pytest tests/ -m "not integration" -v
pytest tests/ -m "not integration" --cov=tools/v1_sync_pipeline --cov-report=term-missing --cov-report=xml
```

Pytest assertions cover markdown parsing utilities plus any helper modules. The `tests` workflow performs the same commands in CI.

## GitHub Actions

### Sync Affinity v1 Docs (`.github/workflows/check-docs-updates.yml`)

- Runs daily at 00:00 UTC and via **Run workflow** in the Actions tab.
- Steps: checkout → install deps → `python tools/v1_sync_pipeline/sync_v1_docs.py --fail-on-diff` → link checker → create PR with `peter-evans/create-pull-request` if changes exist.
- Outputs: PR title `chore: sync Affinity v1 docs`, branch `chore/sync-v1-docs`.

**Manual dispatch:**

1. Navigate to *Actions → Sync Affinity v1 Docs*
2. Click **Run workflow**
3. (Optional) provide a custom ref

### Tests (`.github/workflows/tests.yml`)

- Triggered on push/PR.
- Ensures the repo already contains the generated markdown (`--fail-on-diff`), then runs pytest + coverage.

## Troubleshooting

| Symptom | Checks |
|---------|--------|
| `sync_v1_docs.py` exits >1 | Confirm network access, inspect stack trace, re-run with `-vv` logging if added |
| Link checker reports missing anchors | Inspect recent changes for incorrect headings or duplicate slugs |
| CI sync job opens repeated PRs | Ensure previous PR merged/resolved; pipeline always force-pushes `chore/sync-v1-docs` |
| Tests fail on `--fail-on-diff` | Commit regenerated markdown before pushing |
| Missing snapshots | Verify `tmp/` not deleted mid-run; rerun sync script |

## Checklist Before Submitting Changes

- [ ] `python tools/v1_sync_pipeline/sync_v1_docs.py` (without `--fail-on-diff` after covering diffs)
- [ ] `python tools/v1_sync_pipeline/qa/check_links.py docs/v1/affinity_api_docs.md`
- [ ] `pytest tests/ -m "not integration" -v`
- [ ] `pytest tests/ -m "not integration" --cov=tools/v1_sync_pipeline --cov-report=xml`
- [ ] `git status` clean (only intentional files staged)

## Scheduled Runs

Daily cron is already configured. To temporarily increase cadence for debugging, edit `.github/workflows/check-docs-updates.yml` and adjust the `cron` expression (remember to revert before merging).
