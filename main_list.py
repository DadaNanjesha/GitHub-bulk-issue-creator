from issues.issues_list import ISSUES
from utils.github_api import create_issues_from_list


def main():
    """Main function to create all predefined GitHub issues."""
    print("Starting the process of creating GitHub issues from a list...\n")
    issues_created = create_issues_from_list(ISSUES)
    print(f"Total issues created from list: {issues_created}")


if __name__ == "__main__":
    main()
