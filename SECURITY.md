# Security Policy

## Supported Versions
We prioritize security for the latest release of the project. Critical security updates may be backported to previous versions at our discretion.

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting Vulnerabilities

**Please do not report security vulnerabilities through public GitHub issues.**

### Responsible Disclosure
1. Email security concerns to [MAINTAINER_EMAIL] (or open a private security advisory on GitHub)
2. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Impact analysis
   - Suggested mitigation (if known)
3. We will respond within 3 business days
4. Do not disclose publicly until we've addressed the issue

### Scope
- Authentication token handling
- Data validation/sanitization
- Dependency chain vulnerabilities
- Configuration security

## Security Best Practices for Users

### For CLI Users
1. **Token Security**:
   - Never commit `.env` files or hardcode tokens
   - Use tokens with minimal permissions (only `repo` scope required)
   - Rotate tokens regularly

2. Environment Configuration:
   ```env
   # .env example (keep this file private)
   GITHUB_TOKEN=ghp_yourtokenhere
   GITHUB_REPO_OWNER=your-org
   GITHUB_REPO_NAME=your-repo
   ```

### For Developers
1. Dependency Security:
   ```bash
   # Regularly check for vulnerabilities
   pip list --outdated
   safety check  # Requires `safety` package
   ```

2. Secure Coding:
   - Validate all user input
   - Use Python's built-in security libraries (e.g., `secrets` for tokens)
   - Avoid shell injection risks with subprocess calls

## Maintainer Responsibilities
1. Regular Security Checks:
   - Monitor Python vulnerabilities via [PyPA Security](https://pypi.org/security/)
   - Use GitHub Dependabot for dependency scanning
   ```yaml
   # Example .github/dependabot.yml
   version: 2
   updates:
     - package-ecosystem: "pip"
       directory: "/"
       schedule:
         interval: "weekly"
   ```

2. Response Protocol:
   - Acknowledge report within 3 days
   - Patch development within 14 days
   - Public disclosure after patch release

## Security Tools
We recommend these for development:
- `bandit`: Static code analysis
  ```bash
  pip install bandit
  bandit -r .
  ```
- `safety`: Dependency scanning
  ```bash
  pip install safety
  safety check
  ```

---
