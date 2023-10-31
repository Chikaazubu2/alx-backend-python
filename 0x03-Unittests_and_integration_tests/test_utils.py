#!/usr/bin/env python3
"""
Parameterize unit test
"""
import unittest
from unittest.mock import patch
import requests
from parameterized import parameterized
from utils import(
    access_nested_map,
    get_json
    )


class TestAccessNestedMap(unittest.TestCase):
    """inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test that a KeyError is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test that utils.get_json returns expected result"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """test get_json method"""
        mock_get.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
