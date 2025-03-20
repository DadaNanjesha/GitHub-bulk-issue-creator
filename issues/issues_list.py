# Predefined list of issues to be created in the GitHub repository
# Create as many issues as needed
from config.config import USERNAME

ISSUES = [
    {
        "title": "Set up initial project structure",
        "body": "Create the directory structure for the project, including `data/`, `scripts/`, and `tests/ folders`, and initialize a basic Python environment.",
        "labels": ["Backlog", "Setup", "Project Structure"],
        "assignee": USERNAME,
    },
    {
        "title": "",
        "body": "",
        "labels": ["Backlog", "Feature", "API Integration"],
        "assignee": USERNAME,
    },
    {
        "title": "",
        "body": "",
        "labels": ["Backlog", "Feature", "API Integration"],
        "assignee": USERNAME,
    },
    {
        "title": "",
        "body": "",
        "labels": ["Backlog", "Feature", "Input Processing"],
        "assignee": USERNAME,
    },
    {
        "title": "",
        "body": "",
        "labels": ["Backlog", "Feature", "Vulnerability Scanning"],
        "assignee": USERNAME,
    },
]
