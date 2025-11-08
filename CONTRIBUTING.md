# Contributing to Affinity API Documentation

Thank you for your interest in contributing! This repository contains markdown copies of the official Affinity API documentation.

## How to Contribute

### Reporting Issues

If you notice discrepancies between this documentation and the official Affinity documentation:

1. **Verify** against the [official documentation](https://developer.affinity.co/)
2. **Open an issue** describing:
   - What you found
   - Link to official documentation
   - Suggested fix (if applicable)

### Submitting Changes

1. **Fork the repository**
2. **Create a branch** for your changes
3. **Make your changes**
4. **Ensure pre-commit hooks pass**:

   ```bash
   pip install pre-commit
   pre-commit install
   pre-commit run --all-files
   ```

5. **Run tests**:

   ```bash
   pytest tests/ -m "not integration"
   ```

6. **Submit a pull request**

### Code Style

- **Python**: Follow PEP 8, use type hints, format with black
- **Markdown**: Follow markdownlint rules (configured in `.markdownlint.json`)
- **YAML**: Follow yamllint rules (configured in `.yamllint.yml`)

Pre-commit hooks will automatically check and fix formatting issues.

### Documentation Standards

- Keep documentation accurate and up-to-date
- Follow existing formatting conventions
- Ensure all links work
- Maintain consistency with official Affinity documentation

### Automated Updates

**Note**: This repository uses automated GitHub Actions to sync with official documentation.
Manual updates may be overwritten by automated updates. If you need to make manual changes:

1. Open an issue first to discuss
2. Coordinate with maintainers
3. Ensure changes align with automated update process

### Questions?

- Open an issue for questions or discussions
- Check existing documentation in `docs/development/`
- Review [Testing Guide](docs/development/TESTING.md) and [Pre-commit Guide](docs/development/PRE_COMMIT.md)

## Development Setup

See [Testing Guide](docs/development/TESTING.md) for development setup instructions.

## Code of Conduct

- Be respectful and constructive
- Focus on improving documentation quality
- Follow GitHub's [Community Guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines)
