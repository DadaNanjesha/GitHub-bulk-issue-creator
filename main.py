from issues.issues_list import ISSUES
from utils.github_api import create_issues_from_list


def main():
    """Main function to create all predefined GitHub issues."""
    print("Starting the process of creating GitHub issues...\n")
    create_issues_from_list(ISSUES)


if __name__ == "__main__":
    main()
