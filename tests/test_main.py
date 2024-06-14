"""Module which provides Unittest"""
import unittest
from hello_world.main import fetch_github_api_status


class TestHelloWorld(unittest.TestCase):
    """A Class for unit test"""
    
    def test_fetch_github_api_status(self):
        """Test case for the fetch github api method"""
        result = fetch_github_api_status()
        self.assertIn('Hello, World!', result)


if __name__ == '__main__':
    unittest.main()
