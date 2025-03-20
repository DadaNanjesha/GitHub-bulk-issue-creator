import requests
import json
import csv
from config.config import USERNAME, REPO, TOKEN

# GitHub API URL for creating issues
GITHUB_API_URL = f"https://api.github.com/repos/{USERNAME}/{REPO}/issues"


# Set up headers for authentication
HEADERS = {
    "Authorization": f"token {TOKEN}",
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

    return response

def create_issues_from_list(issues_list):
    """Create multiple issues from a list and return the number of issues created."""
    issues_created = 0  # Counter for successfully created issues

    for issue in issues_list:
        # Create the issue and check if it was successful
        response = create_issue(issue)
        if response.status_code == 201:
            issues_created += 1  # Increment the counter
    issues_created = {f"Total issues created: {issues_created}"}
    return issues_created


def create_issues_from_csv(csv_file_path):
    """Create multiple issues from a CSV file and return the number of issues created."""
    issues_created = 0  # Counter for successfully created issues

    with open(csv_file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert labels from string to list
            labels = row["labels"].split(",") if row["labels"] else []
            # Prepare issue data
            issue_data = {
                "title": row["title"],
                "body": row["body"],
                "labels": labels,
                "assignee": USERNAME,  # Set assignee to the repo owner
            }
            # Create the issue and check if it was successful
            response = create_issue(issue_data)
            if response.status_code == 201:
                issues_created += 1  # Increment the counter

    issues_created = {f"Total issues created: {issues_created}"}
    return issues_created
