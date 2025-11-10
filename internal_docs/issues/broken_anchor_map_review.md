# Quarterly BROKEN_ANCHOR_MAP Review

**Recommended GitHub issue title:** `chore: review BROKEN_ANCHOR_MAP overrides`
**Labels:** `quarterly-review`, `maintenance`
**Milestone target:** 2026-Q1 (run every ~3 months)
**Next review due:** 2026-02-10

## Objective
Confirm the temporary anchor overrides defined in `tools/v1_sync_pipeline/sync_v1_docs.py::BROKEN_ANCHOR_MAP` are still required by the live Affinity API v1 docs. Remove entries that have been fixed upstream and document any new problem anchors.

## Checklist

- [ ] Run `python tools/v1_sync_pipeline/sync_v1_docs.py --fail-on-diff`
- [ ] Compare anchors against the live site; update `BROKEN_ANCHOR_MAP` accordingly
- [ ] Update AGENTS.md Maintenance section with the new "Last reviewed" date
- [ ] Document findings in the issue before closing

## Notes

- Reference link: https://api-docs.affinity.co/
- When filing on GitHub, assign the Docs Automation owner and attach the `automation` label in addition to `quarterly-review`.
