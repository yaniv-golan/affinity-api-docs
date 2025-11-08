# Pre-commit Hooks

This repository uses [pre-commit](https://pre-commit.com/) hooks to ensure code quality and consistency.

## What Gets Checked

### General File Checks

- **Trailing whitespace** - Removes trailing spaces
- **End of file** - Ensures files end with newline
- **YAML validation** - Validates YAML syntax
- **JSON validation** - Validates JSON syntax
- **Large files** - Warns on files > 1MB
- **Merge conflicts** - Detects merge conflict markers
- **Case conflicts** - Detects case-sensitive filename conflicts
- **TOML validation** - Validates TOML files
- **Line endings** - Normalizes to LF

### Python Code Quality

- **black** - Code formatting (auto-fixes)
- **isort** - Import sorting (auto-fixes)
- **ruff** - Fast linting and formatting (auto-fixes)

### Markdown Linting

- **markdownlint** - Validates markdown syntax
- Checks heading hierarchy, list formatting, code blocks, etc.

### YAML Linting

- **yamllint** - Validates YAML files (workflows, configs)

### Custom Checks

- **Documentation structure** - Validates docs/v1/, docs/v2/ exist
- **Version metadata** - Validates JSON structure
- **Workflow paths** - Checks workflow files reference correct paths

## Setup

### Install Pre-commit

```bash
pip install pre-commit
```

### Install Hooks

```bash
pre-commit install
```

This installs git hooks that run automatically on `git commit`.

### Run Manually

```bash
# Run on all files
pre-commit run --all-files

# Run on staged files only
pre-commit run

# Run specific hook
pre-commit run black --all-files
```

## Configuration Files

- **`.pre-commit-config.yaml`** - Main configuration
- **`.markdownlint.json`** - Markdown linting rules
- **`.yamllint.yml`** - YAML linting rules
- **`pyproject.toml`** - Python tooling config (black, isort, ruff)

## CI/CD Integration

Pre-commit checks run automatically in GitHub Actions on:

- Every push to `main`
- Every pull request
- Manual workflow dispatch

See `.github/workflows/pre-commit.yml` for details.

## Auto-fixing

Many hooks can auto-fix issues:

- `black` - Formats Python code
- `isort` - Sorts imports
- `ruff` - Fixes linting issues
- `trailing-whitespace` - Removes trailing spaces
- `end-of-file-fixer` - Adds missing newlines

After hooks run, review the changes and commit them.

## Skipping Hooks

If you need to skip hooks (not recommended):

```bash
git commit --no-verify -m "message"
```

**Note**: This bypasses all checks. Use only when necessary.

## Troubleshooting

### Deprecation Warnings

If you see warnings about deprecated stage names, they have been addressed in our configuration by explicitly setting `stages: [pre-commit]` for hooks that have this issue. This overrides the deprecated stage names defined in the hook repositories themselves.

If you still see warnings after updating hooks, run:

```bash
pre-commit autoupdate --repo https://github.com/pycqa/isort
```

This will update to the latest version that may have fixed the issue.

### Hooks are slow

- First run downloads tools (one-time)
- Subsequent runs use cached tools
- Some hooks (like link checking) can be slow

### Hook fails

- Read the error message
- Most hooks provide fix suggestions
- Auto-fixable hooks will fix issues automatically
- Re-run after fixes: `pre-commit run --all-files`

### Hook not running

- Ensure hooks are installed: `pre-commit install`
- Check `.git/hooks/pre-commit` exists
- Try: `pre-commit run --all-files`

## Updating Hooks

To update hook versions:

```bash
pre-commit autoupdate
```

This updates `.pre-commit-config.yaml` with latest versions.

## Best Practices

1. **Run before committing** - Hooks run automatically, but you can run manually first
2. **Review auto-fixes** - Check what hooks changed before committing
3. **Fix issues locally** - Don't rely on CI to catch issues
4. **Keep hooks updated** - Run `pre-commit autoupdate` periodically
5. **Don't skip hooks** - They catch real issues
