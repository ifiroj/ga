from route import returnString, mode
import unittest, os

class TestMain(unittest.TestCase):
    
    def test_returnString(self):
        string = "apple"
        string_reversed = "elppa"
        self.assertEqual(string_reversed, returnString(string))
    
    def test_get_env(self):
        self.assertEqual(os.environ.get("MODE"), mode())

if __name__ == "__main__":
    unittest.main()