# Contributing to GitHub Issue Creator (Python)

Welcome! This CLI tool for creating GitHub issues is written in Python, and we appreciate your contributions. Below are guidelines to help you get started.

---

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Submitting Pull Requests](#submitting-pull-requests)
- [Local Setup](#local-setup)
- [Development Guidelines](#development-guidelines)
  - [Python Standards](#python-standards)
  - [Testing](#testing)
  - [Documentation](#documentation)
- [Need Help?](#need-help)

---

## Code of Conduct
Read our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a respectful and inclusive environment.

---

## How to Contribute

### Reporting Bugs
1. Check [existing issues](https://github.com/DadaNanjesha/GitHub-issue-creator/issues) first.
2. Include in your report:
   - Python version (`python --version`)
   - Steps to reproduce
   - Expected vs actual behavior
   - Error tracebacks (if applicable)

### Suggesting Features
1. Explain the problem and why your feature solves it.
2. Provide examples of how the feature would work (e.g., new CLI arguments).

### Submitting Pull Requests
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feat/your-feature
   ```
3. Follow [Python Standards](#python-standards).
4. Add tests for new functionality.
5. Update documentation if needed.
6. Open a Pull Request with a clear description.

---

## Local Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/DadaNanjesha/GitHub-issue-creator.git
   cd GitHub-issue-creator
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file with:
   ```env
   GITHUB_TOKEN=your_github_token
   GITHUB_REPO_OWNER=owner_name
   GITHUB_REPO_NAME=repo_name
   ```
   - Get a GitHub token [here](https://github.com/settings/tokens) with `repo` scope.

5. **Run the CLI**:
   ```bash
   python app.py 
   ```

---

## Development Guidelines

### Python Standards
- Follow [PEP 8](https://pep8.org/) style guidelines.
- Use type hints for clarity.
- Format code with **Black**:
  ```bash
  black .
  ```
- Lint with **flake8**:
  ```bash
  flake8
  ```
- Document functions with docstrings (Google-style):
  ```python
  def create_issue(title: str) -> dict:
      """Creates a GitHub issue.
      
      Args:
          title (str): Issue title
      
      Returns:
          dict: API response
      """
  ```

### Testing
- Write tests using **pytest** in the `tests/` directory.
- Run tests with:
  ```bash
  pytest -v
  ```
- Ensure 100% test coverage (if applicable):
  ```bash
  pytest --cov=.
  ```

### Documentation
- Update the README.md for:
  - New CLI arguments/flags
  - Changes to authentication
  - Examples of usage
- Use `argparse` or `click` help strings for CLI documentation.

---

## Need Help?
- Open a [GitHub Issue](https://github.com/DadaNanjesha/GitHub-issue-creator/issues).
- Tag `@DadaNanjesha` in discussions.

---

🚀 Thank you for contributing to this Python project! Your efforts help improve the tool for everyone.
