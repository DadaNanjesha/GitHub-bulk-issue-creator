from utils.github_api import create_issues_from_csv
from config.config import CSV_FILE_PATH
import os

csv_file_path = CSV_FILE_PATH

def main():
    """Main function to create GitHub issues from a CSV file."""
    csv_file_path = "issues.csv"  # Ensure this path is correct
    print(f"CSV file path: {csv_file_path}")  # Debugging statement

    # Check if the file exists
    if not os.path.exists(csv_file_path):
        print(f"Error: The file '{csv_file_path}' does not exist.")
        return

    print("Starting the process of creating GitHub issues from a CSV file...\n")
    issues_created = create_issues_from_csv(csv_file_path)
    print(issues_created)


if __name__ == "__main__":
    main()
