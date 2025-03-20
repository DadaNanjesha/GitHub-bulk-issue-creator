import unittest
from unittest.mock import patch, Mock, mock_open
import json
from utils.github_api import create_issue, create_issues_from_list, create_issues_from_csv
import os
from config.config import USERNAME, REPO, TOKEN


class TestGitHubAPI(unittest.TestCase):

    def setUp(self):
        """Set up before each test"""
        self.patcher = patch.dict(
            os.environ,
            {
                "USERNAME": USERNAME,  # Mocked GitHub username
                "REPO": REPO,  # Mocked repository name
                "TOKEN": TOKEN,  # Mocked GitHub token
            },
        )
        self.patcher.start()


        self.test_issue = {
            "title": "Test Issue",
            "body": "This is a test issue",
            "labels": ["bug"],
            "assignee": USERNAME,  # Updated to use USERNAME
        }
        self.api_url = f"https://api.github.com/repos/{USERNAME}/{REPO}/issues"
        self.headers = {
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }

    @patch("requests.post")
    def test_create_issue(self, mock_post):
        """Test creating a single issue"""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "id": 1,
            "title": "Test Issue",
            "body": "This is a test issue",
            "labels": ["bug"],
            "assignee": USERNAME,
        }
        mock_post.return_value = mock_response

        # Call the function
        response = create_issue(self.test_issue)

        # Assert that the API was called with the correct parameters
        mock_post.assert_called_once_with(
            self.api_url, headers=self.headers, data=json.dumps(
                self.test_issue)
        )

        # Check if the response matches the expected status
        self.assertEqual(response.json()["title"], "Test Issue")
        self.assertEqual(response.status_code, 201)

    @patch("requests.post")
    def test_create_multiple_issues(self, mock_post):
        """Test creating multiple issues"""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "id": 1,
            "title": "Test Issue",
            "body": "This is a test issue",
            "labels": ["bug"],
            "assignee": USERNAME,
        }
        mock_post.return_value = mock_response

        issues_list = [
            {
                "title": "Issue 1",
                "body": "This is the first test issue",
                "labels": ["bug"],
                "assignee": USERNAME,
            },
            {
                "title": "Issue 2",
                "body": "This is the second test issue",
                "labels": ["enhancement"],
                "assignee": USERNAME,
            },
        ]

        # Call the function and get the number of issues created
        issues_created = create_issues_from_list(issues_list)

        # Check that the API was called twice (once for each issue)
        self.assertEqual(mock_post.call_count, 2)

        # Check that the number of issues created matches the expected count
        self.assertEqual(issues_created, {f"Total issues created: 2"})

    @patch("requests.post")
    def test_create_issue_failure(self, mock_post):
        """Test failure to create an issue due to API error"""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"message": "Bad Request"}
        mock_post.return_value = mock_response

        # Simulate calling the create_issue function and assert the response
        response = create_issue(self.test_issue)

        # Assert that the response matches the expected error structure
        self.assertEqual(response.json(), {"message": "Bad Request"})
        self.assertEqual(response.status_code, 400)

    @patch("requests.post")
    def test_create_issue_missing_data(self, mock_post):
        """Test missing data during issue creation"""
        incomplete_issue = {
            "title": "Missing Body",
            "labels": ["bug"],
            "assignee": USERNAME,
        }

        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"message": "Bad Request"}
        mock_post.return_value = mock_response

        # Simulate calling the create_issue function with missing data
        response = create_issue(incomplete_issue)

        # Assert that the response matches the expected error structure
        self.assertEqual(response.json(), {"message": "Bad Request"})
        self.assertEqual(response.status_code, 400)

    @patch("requests.post")
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="title,body,labels\nIssue 1,This is issue 1,bug\nIssue 2,This is issue 2,enhancement",
    )
    def test_create_issues_from_csv(self, mock_file, mock_post):
        """Test creating issues from a CSV file"""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "id": 1,
            "title": "Test Issue",
            "body": "This is a test issue",
            "labels": ["bug"],
            "assignee": USERNAME,
        }
        mock_post.return_value = mock_response

        # Call the function
        csv_file_path = "issues.csv"
        issues_created = create_issues_from_csv(csv_file_path)

        # Assert that the file was opened correctly
        mock_file.assert_called_once_with(
            csv_file_path, mode="r", newline="", encoding="utf-8"
        )

        # Check that the API was called twice (once for each issue in the CSV)
        self.assertEqual(mock_post.call_count, 2)

        # Check that the number of issues created matches the expected count
        self.assertEqual(issues_created, {f"Total issues created: 2"})


if __name__ == "__main__":
    unittest.main()
