import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr_1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")
    
    def test_repr_2(self):
        loc = Location('San Francisco', 123.2, 432)
        self.assertEqual(repr(loc), "Location('San Francisco', 123.2, 432)")

    def test_repr_3(self):
        loc = Location('Vegas', 444, 2.33)
        self.assertEqual(repr(loc), "Location('Vegas', 444, 2.33)")

    def test_eq_1(self):
        loc1 = Location("SLO", 12.1, -14.2)
        loc2 = Location("SLO", 12.1, -14.2)
        self.assertTrue(loc1 == loc2)

    def test_eq_2(self):
        loc1 = Location("SF", 123, 543)
        loc2 = Location("SF", 124, 543)
        self.assertFalse(loc1 == loc2)

    def test_eq_3(self):
        loc1 = Location("Vegas", 43.2, -12.3)
        loc2 = Location("Vegas", 43.2, 12.3)
        self.assertFalse(loc1 == loc2)


if __name__ == "__main__":
        unittest.main()
