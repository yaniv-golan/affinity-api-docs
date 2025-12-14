# AGENTS.md

## Project Overview

This repository hosts the automatically generated **Affinity API v1** and **API v2** documentation. The canonical markdown is created by the sync pipelines and **must never be edited manually**—run the tooling instead.

- **Primary doc (v1):** `docs/v1/affinity_api_docs.md` (auto-generated)
- **Primary doc (v2):** `docs/v2/affinity_api_docs.md` (auto-generated)
- **OpenAPI spec (v2):** `docs/v2/openapi.json` (auto-generated)
- **Automation:** `tools/v1_sync_pipeline/` and `tools/v2_sync_pipeline/` (sync + QA tooling)

## Current Status

- ✅ v1 markdown extracted, normalized, and auto-synced from https://api-docs.affinity.co/
- ✅ v2 markdown extracted from the Redoc OpenAPI payload at https://developer.affinity.co/ with flattened schemas, synthesized cURL examples, and schema appendices
- ✅ Code samples + JSON payloads match the live sites; the parsers auto-detect new fenced code languages when Affinity adds them
- ✅ Last-updated timestamps injected automatically during sync
- ✅ Legacy manual doc preserved separately with warning banner
- ✅ CI schedules daily syncs and opens PRs when drift is detected
- ✅ QA scripts (link checker + live comparison helper) live under `tools/v1_sync_pipeline/qa/`

## Automation Workflow

### Sync Scripts

- **v1:** `python tools/v1_sync_pipeline/sync_v1_docs.py [--fail-on-diff]`
  - Reads https://api-docs.affinity.co/, writes `docs/v1/affinity_api_docs.md`, snapshot artifacts under `tmp/`
- **v2:** `python tools/v2_sync_pipeline/sync_v2_docs.py [--fail-on-diff]`
  - Reads https://developer.affinity.co/, writes `docs/v2/affinity_api_docs.md` and `docs/v2/openapi.json`, HTML/state JSON/manifest saved under `tmp/v2/`
  - Automatically extracts the embedded Redoc OpenAPI JSON, dereferences `$ref`s, flattens schemas, and injects schema + error appendices
  - `--fail-on-diff` mirrors the v1 behavior (exit 1 when the output differs from what is committed)

### QA Scripts

- `python tools/v1_sync_pipeline/qa/check_links.py [PATH]` – validates internal anchors and external HTTP links (defaults to the canonical doc). Use it for both v1 and v2 by pointing at the desired markdown file.
- `python tools/v1_sync_pipeline/qa/compare_to_live.py --snapshot tmp/current_live_site.html` – helper for comparing markdown vs. captured browser snapshots (v1 only today).

### CI/CD

- **Sync Affinity Docs** (`.github/workflows/check-docs-updates.yml`): runs daily + on demand, executes both sync scripts, runs the link checker against v1 and v2 output, and opens a PR via `peter-evans/create-pull-request` when either doc changes.
- **Tests** (`.github/workflows/tests.yml`): runs on push/PR, installs dependencies, verifies both sync scripts with `--fail-on-diff`, runs the link checker, and executes the pytest suite with coverage over `tools/v1_sync_pipeline` and `tools/v2_sync_pipeline`.

## Maintenance & Ownership

1. **Never edit** `docs/v1/affinity_api_docs.md`, `docs/v2/affinity_api_docs.md`, or `docs/v2/openapi.json` manually. Regenerate via the sync scripts whenever updates are needed.
2. **Quarterly BROKEN_ANCHOR_MAP review:** revisit `BROKEN_ANCHOR_MAP` inside `sync_v1_docs.py`, confirm the live site still requires the overrides, and track the reminder in the quarterly review issue (label `quarterly-review`).
3. **Manual validation checklist (when investigating diffs):**
   - Run `python tools/v1_sync_pipeline/sync_v1_docs.py` and `python tools/v2_sync_pipeline/sync_v2_docs.py`
   - Run `python tools/v1_sync_pipeline/qa/check_links.py docs/v1/affinity_api_docs.md` and the same command pointing at `docs/v2/affinity_api_docs.md`
   - Optionally run `python tools/v1_sync_pipeline/qa/compare_to_live.py --snapshot <new snapshot>` for v1 HTML diffs
   - Run `python -m pytest`
4. **llms.txt** contains explicit “DO NOT EDIT” warnings for AI assistants—keep it updated when automation changes.
5. **Example overrides & metadata:** keep `tools/v1_sync_pipeline/example_overrides.yml` in sync with any upstream discrepancies, and ensure `tmp/v1_sync_metadata.json` reports an empty `example_mismatches` array. Content/label hygiene fixes are automated—do not revert them in the generated markdown. The v2 pipeline currently synthesizes cURL examples from the OpenAPI payload; if Affinity adds native code samples we can extend the renderer instead of editing the markdown.

## Project Structure (trimmed)

```
affinity-api-docs/
├── AGENTS.md (this file)
├── README.md
├── REPOSITORY_STRUCTURE.md
├── docs/
│   ├── v1/
│   │   └── affinity_api_docs.md          # auto-generated canonical doc
│   ├── v2/
│   │   └── affinity_api_docs.md          # auto-generated canonical doc
│   │   └── openapi.json                  # auto-generated OpenAPI spec
│   └── development/
├── tools/
│   └── v1_sync_pipeline/
│       ├── sync_v1_docs.py               # v1 production sync pipeline
│       └── qa/
│           ├── check_links.py
│           └── compare_to_live.py
│   └── v2_sync_pipeline/
│       ├── sync_v2_docs.py               # v2 production sync pipeline
│       ├── openapi_loader.py
│       └── markdown_renderer.py
├── .github/
│   ├── workflows/
│   │   ├── check-docs-updates.yml        # daily sync + auto-PR
│   │   ├── pre-commit.yml
│   │   └── tests.yml                     # CI tests + sync verification
│   └── scripts/
│       └── validate_docs_structure.py
├── tests/
│   ├── test_documentation_updates.py
│   └── test_v2_sync_pipeline.py
├── tmp/ (gitignored artifacts: snapshots, extracted blocks, comparisons)
└── internal_docs/ … (project reports & planning)
```

## Important Notes

- `docs/v1/affinity_api_docs.md` and `docs/v2/affinity_api_docs.md` are generated—**editing them manually will be reverted** the next time the pipelines run.
- `docs/v2/openapi.json` is generated—**editing it manually will be reverted** the next time the v2 pipeline runs.
- `docs/internal/` is gitignored on purpose—keep planning/rollout notes there locally without committing them.
- The sync header clearly states the unofficial nature of this copy; always cross-check with https://api-docs.affinity.co/.
- `llms.txt` spells out the guardrails for AI assistants—review it before delegating tasks to LLMs.
- Use fenced code blocks (`bash`, `ruby`, `python`, `javascript`, `json`) exactly as produced by the pipeline.

## Authentication

- **Affinity API v1:** supports HTTP Basic Auth (API key as password, username blank) or Bearer token (`Authorization: Bearer YOUR_API_KEY`).
- **Affinity API v2:** uses Bearer tokens only (mirrored at `docs/v2/affinity_api_docs.md` from https://developer.affinity.co/).

## Resources & Support

- Live Docs: https://api-docs.affinity.co/
- Repo Docs (auto-generated): `docs/v1/affinity_api_docs.md`, `docs/v2/affinity_api_docs.md`
- Support: [support@affinity.co](mailto:support@affinity.co)
- Issues/automation reminders: see GitHub issues labeled `quarterly-review` (BROKEN_ANCHOR_MAP) and `automation`.

## API Version Differences

- v1 and v2 are separate APIs with distinct schemas and auth strategies.
- v1 base URL: `https://api.affinity.co/`
- v2 base URL: `https://api.affinity.co/v2`
- Do **not** assume parity between versions; maintain both docs independently.
