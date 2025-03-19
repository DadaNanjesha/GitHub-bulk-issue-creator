from utils.github_api import create_issues_from_csv
from config.config import CSV_FILE_PATH

csv_file_path = CSV_FILE_PATH


def main():
    """Main function to create GitHub issues from a CSV file."""
    print("Starting the process of creating GitHub issues from a CSV file...\n")
    issues_created = create_issues_from_csv(csv_file_path)
    print(f"Total issues created from CSV: {issues_created}")


if __name__ == "__main__":
    main()
