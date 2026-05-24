"""
Unit tests for hello.py
"""

import unittest
from hello import greet


class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""

    def test_greet_default(self):
        """Test greeting with default parameter."""
        self.assertEqual(greet(), "Hello, World!")

    def test_greet_with_name(self):
        """Test greeting with custom name."""
        self.assertEqual(greet("GitHub"), "Hello, GitHub!")
        self.assertEqual(greet("Claude"), "Hello, Claude!")

    def test_greet_empty_string(self):
        """Test greeting with empty string."""
        self.assertEqual(greet(""), "Hello, !")


if __name__ == '__main__':
    unittest.main()
