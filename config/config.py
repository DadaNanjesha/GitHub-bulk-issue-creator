import os
from dotenv import load_dotenv

load_dotenv()

# GitHub username or organization name or add new var
USERNAME = os.getenv("USERNAME")
# The repository name where issues will be created
REPO = os.getenv("REPO")
# GitHub Personal Access Token for authentication
TOKEN = os.getenv("GITHUB_TOKEN")  # Your GitHub personal access token
# Path to your CSV file
CSV_FILE_PATH = "issues.csv"


# Verify that the environment variables are loaded
if not all([USERNAME, REPO, TOKEN]):
    raise ValueError(
        "Please ensure all environment variables (USERNAME, REPO, TOKEN) are set in the .env file."
    )
