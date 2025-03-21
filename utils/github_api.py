import requests
import json
import csv


def create_issue(issue_data, USERNAME, REPO, TOKEN):
    """Create an issue in the GitHub repository using GitHub API."""
    try:
        GITHUB_API_URL = f"https://api.github.com/repos/{USERNAME}/{REPO}/issues"
        print(GITHUB_API_URL)
        HEADERS = {
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.post(
            GITHUB_API_URL, headers=HEADERS, data=json.dumps(issue_data)
        )
        if response.status_code == 201:
            print(f"Issue '{issue_data['title']}' created successfully.")
        else:
            print(
                f"Failed to create issue '{issue_data['title']}': {response.content}")
    except requests.exceptions.RequestException as e:
        print(f"API Error: {str(e)}")
        return None

    return response

def create_issues_from_list(issues_list):
    """Create multiple issues from a list and return the number of issues created."""
    from config.config import USERNAME, REPO, TOKEN
    issues_created = 0  # Counter for successfully created issues

    for issue in issues_list:
        # Create the issue and check if it was successful
        response = create_issue(issue, USERNAME, REPO, TOKEN)
        if response.status_code == 201:
            issues_created += 1  # Increment the counter
    issues_created = {f"Total issues created: {issues_created}"}
    return issues_created


def create_issues_from_csv(csv_file_path, USERNAME, REPO, TOKEN):
    """Create multiple issues from a CSV file and return the number of issues created."""
    issues_created = 0  # Counter for successfully created issues

    # checck if csv_file_path is is .csv file or StringIO from streamlit
    if isinstance(csv_file_path, str):
        csv_file_path = open(csv_file_path, mode="r",
                             newline="", encoding="utf-8")
        reader = csv.DictReader(csv_file_path)
    else:
        reader = csv.DictReader(csv_file_path)

    for row in reader:
        # Clean and split labels
        raw_labels = row.get("labels", "")
        labels = [label.strip().strip('"')
                  for label in raw_labels.split(",") if label.strip()]

        # Prepare issue data
        issue_data = {
            "title": row["title"],
            "body": row["body"],
            "labels": labels,
            "assignee": USERNAME,
        }

        # Create the issue and check if it was successful
        response = create_issue(issue_data, USERNAME, REPO, TOKEN)
        if response.status_code == 201:
            issues_created += 1
        else:
            print(
                f"Failed to create issue '{row['title']}': {response.content}")

    return {f"Total issues created: {issues_created}"}
