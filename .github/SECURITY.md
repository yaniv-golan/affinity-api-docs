# Security Policy

## Supported Versions

This repository maintains documentation for:

- **Affinity API v1** (Legacy)
- **Affinity API v2** (Current)

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please **do not** open a public issue.

Instead, please report it via one of the following methods:

1. **Email**: Send details to the repository maintainers (check repository settings for contact)
2. **Private Security Advisory**: Use GitHub's private security advisory feature
3. **Direct Message**: Contact repository maintainers directly

### What to Include

When reporting a vulnerability, please include:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Response Time

We will acknowledge receipt of your report within 48 hours and provide an update within 7 days.

## Security Considerations

### This Repository

This repository contains:

- **Documentation only** - No executable code or services
- **Public API documentation** - Already publicly available
- **Automated update scripts** - Run in controlled CI/CD environment

### Security Best Practices

- All workflows run with minimal required permissions
- No secrets or credentials stored in repository
- Automated updates are reviewed before merging
- Pre-commit hooks prevent common security issues

### External Dependencies

This repository uses:

- GitHub Actions (official actions only)
- Python packages (listed in `requirements-ci.txt`)
- Pre-commit hooks (from official repositories)

All dependencies are regularly updated and monitored.

## Disclosure Policy

- Vulnerabilities will be disclosed after they are fixed
- Credit will be given to reporters (if desired)
- Fixes will be included in the next release

## Security Updates

Security updates are applied via:

- Automated dependency updates (when configured)
- Manual updates by maintainers
- Pull requests from security researchers

Thank you for helping keep this repository secure!
