import unittest
from unittest.mock import patch
import json
from utils.github_api import create_issue, create_issues_from_list
from config.config import USERNAME, REPO, TOKEN

class TestGitHubAPI(unittest.TestCase):

    def setUp(self):
        """Set up before each test"""
        self.test_issue = {
            "title": "Test Issue",
            "body": "This is a test issue",
            "labels": ["bug"],
            "assignee": None,
        }
        self.api_url = f"https://api.github.com/repos/{USERNAME}/{REPO}/issues"
        self.headers = {
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }

    @patch("requests.post")
    def test_create_issue(self, mock_post):
        """Test creating a single issue"""
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            "id": 1,
            "title": "Test Issue",
            "body": "This is a test issue",
            "labels": ["bug"],
            "assignee": None,
        }

        response = create_issue(self.test_issue)

        # Assert that the API was called with the correct parameters
        mock_post.assert_called_once_with(
            self.api_url, headers=self.headers, data=json.dumps(self.test_issue)
        )

        # Check if the response matches the expected status
        self.assertEqual(response["title"], "Test Issue")
        self.assertEqual(response["body"], "This is a test issue")

    @patch("requests.post")
    def test_create_multiple_issues(self, mock_post):
        """Test creating multiple issues"""
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            "id": 1,
            "title": "Test Issue",
            "body": "This is a test issue",
            "labels": ["bug"],
            "assignee": None,
        }

        issues_list = [
            {
                "title": "Issue 1",
                "body": "This is the first test issue",
                "labels": ["bug"],
                "assignee": None,
            },
            {
                "title": "Issue 2",
                "body": "This is the second test issue",
                "labels": ["enhancement"],
                "assignee": None,
            },
        ]

        create_issues_from_list(issues_list)

        # Check that the API was called twice (once for each issue)
        self.assertEqual(mock_post.call_count, 2)

    @patch("requests.post")
    def test_create_issue_failure(self, mock_post):
        """Test failure to create an issue due to API error"""
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {"message": "Bad Request"}

        response = create_issue(self.test_issue)

        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response, {"message": "Bad Request"})

    @patch("requests.post")
    def test_create_issue_missing_data(self, mock_post):
        """Test missing data during issue creation"""
        # Create an issue without required fields like 'title' or 'body'
        incomplete_issue = {
            "title": "Missing Body",
            "labels": ["bug"],
            "assignee": None,
        }

        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {"message": "Bad Request"}

        response = create_issue(incomplete_issue)

        # Assert that the response status code is 400 due to missing 'body'
        self.assertEqual(response, {"message": "Bad Request"})


if __name__ == "__main__":
    unittest.main()
