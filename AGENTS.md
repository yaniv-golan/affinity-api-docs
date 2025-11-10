# AGENTS.md

## Project Overview

This repository hosts the automatically generated **Affinity API v1** documentation alongside the scaffolding for future v2 work. The canonical markdown is created by the sync pipeline and **must never be edited manually**—run the tooling instead.

- **Primary doc:** `docs/v1/affinity_api_docs.md` (auto-generated)
- **Automation:** `tools/v1_sync_pipeline/` (sync + QA tooling)

## Current Status

- ✅ Markdown extracted, normalized, and auto-synced from https://api-docs.affinity.co/
- ✅ Code samples match the live site (currently bash/cURL + JSON) and the parser auto-detects new languages as they appear
- ✅ Last-updated timestamp injected automatically during sync
- ✅ Legacy manual doc preserved separately with warning banner
- ✅ CI schedules daily syncs and opens PRs when drift is detected
- ✅ QA scripts (link checker + live comparison helper) live under `tools/v1_sync_pipeline/qa/`
- ⚠️ Future work: add Affinity API v2 documentation when ready

## Automation Workflow

### Sync Script

- Path: `tools/v1_sync_pipeline/sync_v1_docs.py`
- Usage: `python tools/v1_sync_pipeline/sync_v1_docs.py [--fail-on-diff]`
- Defaults: reads from `https://api-docs.affinity.co/`, writes to `docs/v1/affinity_api_docs.md`, stores HTML + metadata in `tmp/`
- `--fail-on-diff` exits with code 1 if the generated markdown differs from what is committed (used by CI/tests)

### QA Scripts

- `python tools/v1_sync_pipeline/qa/check_links.py [PATH]` – validates internal anchors and external HTTP links (defaults to the canonical doc)
- `python tools/v1_sync_pipeline/qa/compare_to_live.py --snapshot tmp/current_live_site.html` – helper for comparing markdown vs. captured browser snapshots

### CI/CD

- **Sync Affinity v1 Docs** (`.github/workflows/check-docs-updates.yml`): runs daily + on demand, executes the sync script with `--fail-on-diff`, runs the link checker, and opens a PR via `peter-evans/create-pull-request` when changes exist.
- **Tests** (`.github/workflows/tests.yml`): runs on push/PR, installs dependencies, executes the sync script with `--fail-on-diff`, and runs the pytest suite with coverage over `tools/v1_sync_pipeline`.

## Maintenance & Ownership

1. **Never edit** `docs/v1/affinity_api_docs.md` manually. Regenerate via the sync script whenever updates are needed.
2. **Quarterly BROKEN_ANCHOR_MAP review:** revisit `BROKEN_ANCHOR_MAP` inside `sync_v1_docs.py`, confirm the live site still requires the overrides, and track the reminder in the quarterly review issue (label `quarterly-review`).
3. **Manual validation checklist (when investigating diffs):**
   - Run `python tools/v1_sync_pipeline/sync_v1_docs.py`
   - Run `python tools/v1_sync_pipeline/qa/check_links.py docs/v1/affinity_api_docs.md`
   - Optionally run `python tools/v1_sync_pipeline/qa/compare_to_live.py --snapshot <new snapshot>`
   - Run `pytest tests/`
4. **llms.txt** contains explicit “DO NOT EDIT” warnings for AI assistants—keep it updated when automation changes.
5. **Example overrides & metadata:** keep `tools/v1_sync_pipeline/example_overrides.yml` in sync with any upstream discrepancies, and ensure `tmp/v1_sync_metadata.json` reports an empty `example_mismatches` array. Content/label hygiene fixes are automated—do not revert them in the generated markdown.

## Project Structure (trimmed)

```
affinity-api-docs/
├── AGENTS.md (this file)
├── README.md
├── REPOSITORY_STRUCTURE.md
├── docs/
│   ├── v1/
│   │   └── affinity_api_docs.md          # auto-generated canonical doc
│   ├── v2/                               # placeholder for future work
│   └── development/
├── tools/
│   └── v1_sync_pipeline/
│       ├── sync_v1_docs.py               # production sync pipeline
│       └── qa/
│           ├── check_links.py
│           └── compare_to_live.py
├── .github/
│   ├── workflows/
│   │   ├── check-docs-updates.yml        # daily sync + auto-PR
│   │   ├── pre-commit.yml
│   │   └── tests.yml                     # CI tests + sync verification
│   └── scripts/
│       └── validate_docs_structure.py
├── tests/
│   └── test_documentation_updates.py
├── tmp/ (gitignored artifacts: snapshots, extracted blocks, comparisons)
└── internal_docs/ … (project reports & planning)
```

## Important Notes

- `docs/v1/affinity_api_docs.md` is generated—**editing it manually will be reverted** the next time the pipeline runs.
- `docs/internal/` is gitignored on purpose—keep planning/rollout notes there locally without committing them.
- The sync header clearly states the unofficial nature of this copy; always cross-check with https://api-docs.affinity.co/.
- `llms.txt` spells out the guardrails for AI assistants—review it before delegating tasks to LLMs.
- Use fenced code blocks (`bash`, `ruby`, `python`, `javascript`, `json`) exactly as produced by the pipeline.

## Authentication

- **Affinity API v1:** supports HTTP Basic Auth (API key as password, username blank) or Bearer token (`Authorization: Bearer YOUR_API_KEY`).
- **Affinity API v2:** uses Bearer tokens only (v2 docs live at https://developer.affinity.co/ and are not yet mirrored here).

## Resources & Support

- Live Docs: https://api-docs.affinity.co/
- Repo Docs (auto-generated): `docs/v1/affinity_api_docs.md`
- Support: [support@affinity.co](mailto:support@affinity.co)
- Issues/automation reminders: see GitHub issues labeled `quarterly-review` (BROKEN_ANCHOR_MAP) and `automation`.

## API Version Differences

- v1 and v2 are separate APIs with distinct schemas and auth strategies.
- v1 base URL: `https://api.affinity.co/`
- v2 base URL: `https://api.affinity.co/v2`
- Do **not** assume parity between versions; maintain both docs independently.
