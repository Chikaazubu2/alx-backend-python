#!/usr/bin/env python3
"""
TestGithubOrgClient module
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_res):
        """
        test that GithubOrgClient.org
        returns the correct value
        """
        endpoint = f"https://api.github.com/orgs/{org_name}"

        class_instance = GithubOrgClient(org_name)
        class_instance.org()
        mock_res.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("some-url", {'repos_url': 'http://some_url.com'}),
    ])
    def test_public_repos_url(self, name, res):
        """
        tests public_repo_url
        """
        with patch(
            "client.GithubOrgClient.org", PropertyMock(return_value=res)
        ):
            mock_res = GithubOrgClient(name)._public_repos_url
            self.assertEqual(mock_res, res.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, mock_get):
        """
        tests public_repos
        """
        payload = [{"name": "google"}, {"name": "facebook"}]
        mock_get.return_value = payload

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock:
            mock.return_value = "Hello"
            response = GithubOrgClient("test").public_repos()

            self.assertEqual(response, ["google", "facebook"])

            mock.assert_called_once()
            mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, licens, license_key, expected_result):
        self.assertEqual(
            GithubOrgClient.has_license(licens, license_key),
            expected_result
        )


@parameterized_class([
    'org_payload', 'repos_payload',
    'expected_repos', 'apache2_repos'],
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    TestIntegrationGithubOrgClient module
    """
    @classmethod
    def setUpClass(cls):
        """
        mock requests.get to return
        example payloads found in the fixtures
        """
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass class method
        to stop the patcher
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        test_public_repos
        """

    def test_public_repos_with_license(self):
        """
        test public_with_license
        """


if __name__ == "__main__":
    unittest.main()
