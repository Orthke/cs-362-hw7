import unittest
from leap_year import leap_year

class TestStringMethods(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(leap_year(2000), True)

if __name__ == "__main__":
    unittest.main()