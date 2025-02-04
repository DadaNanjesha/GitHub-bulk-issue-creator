import requests
import json
from config.config import GITHUB_USERNAME, GITHUB_REPO, GITHUB_TOKEN

# GitHub API URL for creating issues
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/issues"

# Set up headers for authentication
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}


def create_issue(issue_data):
    """Create an issue in the GitHub repository using GitHub API."""
    response = requests.post(
        GITHUB_API_URL, headers=HEADERS, data=json.dumps(issue_data)
    )
    if response.status_code == 201:
        print(f"Issue '{issue_data['title']}' created successfully.")
    else:
        print(f"Failed to create issue '{issue_data['title']}': {response.content}")


def create_issues_from_list(issues_list):
    """Create multiple issues from a list."""
    for issue in issues_list:
        create_issue(issue)
