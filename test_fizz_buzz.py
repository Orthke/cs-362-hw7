import unittest

class TestStringMethods(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizz_buzz(3), "Fizz")

if __name__ == "__main__":
    unittest.main()