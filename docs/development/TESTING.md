# Testing the Documentation Update Workflow

This guide explains how to test the automated documentation update workflow.

## Test Framework

We use **pytest** for testing, which provides better test organization, fixtures, and reporting compared to custom scripts.

## Prerequisites

1. **Python 3.11+** installed locally
2. **GitHub CLI (`gh`)** installed and authenticated (for integration tests)
3. **Dependencies** installed: `pip install -r requirements-ci.txt`

## Testing Methods

### 1. Run Pytest Tests - RECOMMENDED

Run the pytest test suite:

```bash
# Install dependencies
pip install -r requirements-ci.txt

# Run all unit tests (fast, no network)
pytest tests/ -m "not integration"

# Run all tests including integration tests
pytest tests/ -v

# Run specific test class
pytest tests/test_documentation_updates.py::TestContentExtraction -v

# Run with coverage
pytest tests/ --cov=.github/scripts --cov-report=html
```

### 2. Dry-Run Testing

Test the Python script locally without creating PRs:

```bash
# Test with dry-run mode (safest - no PRs or commits)
python .github/scripts/check_and_update_docs.py --api-version v1 --dry-run

# Or use the legacy test script
./tests/test-local.sh
```

**What to check:**

- Script fetches HTML from the website successfully
- Timestamp extraction works
- Content comparison detects changes (or lack thereof)
- Dry-run output shows what would happen (branch name, diff summary, PR title)
- No errors in the output

### 3. Manual GitHub Actions Workflow Trigger

The easiest way to test the full workflow:

1. **Go to GitHub Actions tab** in your repository
2. **Click on "Check Documentation Updates"** workflow
3. **Click "Run workflow"** button (top right)
4. **Select options:**
   - API version: `v1` (or `all`)
   - Force check: `true` (to bypass time-based checks)
5. **Click "Run workflow"**

**What to check:**

- Workflow runs successfully
- All steps complete without errors
- If changes detected: PR is created
- If no changes: workflow exits cleanly

### 4. Test with Force Check

Force the workflow to check even if recently checked:

```bash
# Via GitHub CLI
gh workflow run "Check Documentation Updates" \
  -f api_version=v1 \
  -f force_check=true
```

### 5. Simulate Changes (Advanced)

To test the PR creation logic, you can:

1. **Temporarily modify the comparison logic** to always detect changes:

   ```python
   # In check_and_update_docs.py, temporarily change:
   has_changes, reason = compare_versions(...)
   # To:
   has_changes, reason = True, "Test change"
   ```

2. **Or manually edit** the version metadata file to simulate an old check:

   ```bash
   # Edit .github/docs-version-v1.json
   # Change "last_checked" to an old date
   ```

### 6. Check Workflow Logs

After running the workflow:

1. Go to **Actions** tab
2. Click on the latest workflow run
3. Expand each step to see logs
4. Check for any errors or warnings

### 7. Verify PR Creation

If a PR was created, verify:

- [ ] PR title is correct format
- [ ] PR description includes change summary
- [ ] PR has correct labels (`auto-update`, `documentation`)
- [ ] Branch name follows pattern: `docs/auto-update-v1-YYYY-MM-DD-{hash}`
- [ ] Documentation file has updated timestamp in header
- [ ] Notice section was added to documentation

### 8. Test Duplicate Prevention

To test that duplicate PRs aren't created:

1. Run the workflow once (creates PR if changes detected)
2. Run it again immediately
3. Verify: Second run should detect existing PR and skip creation

### 9. Test Error Handling

Test various error scenarios:

**Network failure:**

- Temporarily block network access (not recommended)
- Or modify script to use invalid URL

**Missing file:**

- Test with v2 (which doesn't have docs yet) - should skip gracefully

**Git errors:**

- Test in a non-git directory (should fail gracefully)

## Quick Test Checklist

- [ ] Script runs locally without errors
- [ ] Workflow can be manually triggered
- [ ] Workflow completes successfully
- [ ] PR creation works (if changes detected)
- [ ] Header timestamp updates correctly
- [ ] Notice section is added
- [ ] Duplicate PRs are prevented
- [ ] Error handling works gracefully

## Troubleshooting

### Workflow fails at "Check and update documentation"

- Check Python script syntax: `python -m py_compile .github/scripts/check_and_update_docs.py`
- Verify dependencies are installed
- Check GitHub Actions logs for specific error

### PR not created

- Check if changes were actually detected (look at workflow logs)
- Verify GitHub token has correct permissions
- Check if PR already exists for this version

### Header not updating

- Check regex patterns match your header format
- Look at script output for pattern matching messages
- Verify file permissions

### GitHub CLI errors

- Ensure `gh` is installed in workflow
- Check authentication: `gh auth status`
- Verify token permissions

## Testing Schedule

The workflow runs automatically **daily at 00:00 UTC**. To test the scheduled run:

1. Wait for the scheduled time, OR
2. Temporarily change the cron schedule to run sooner:

   ```yaml
   # In .github/workflows/check-docs-updates.yml
   schedule:
     - cron: '*/5 * * * *'  # Every 5 minutes (for testing only!)
   ```

   **Remember to change it back!**

## Next Steps After Testing

Once testing is complete:

1. Verify all checks pass
2. Monitor first few automated runs
3. Review PRs created by the workflow
4. Adjust thresholds or logic if needed
5. Document any custom configurations
