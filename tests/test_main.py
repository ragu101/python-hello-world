import unittest
from hello_world.main import fetch_github_api_status

class TestHelloWorld(unittest.TestCase):
    
    def test_fetch_github_api_status(self):
        result = fetch_github_api_status()
        self.assertIn('Hello, World!', result)

if __name__ == '__main__':
    unittest.main()
