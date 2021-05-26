import unittest
from leap_year import leap_year

class TestStringMethods(unittest.TestCase):

    def test_divis4(self):
        self.assertEqual(leap_year(2000), False)

    def test_divis100(self):
        self.assertEqual(leap_year(2100), False)

    def test_divis100(self):
        self.assertEqual(leap_year(2400), True)

if __name__ == "__main__":
    unittest.main()