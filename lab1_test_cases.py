import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_1(self):
        """passes None lists and checks if ValueError is raised"""
        t_list = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(t_list)

    def test_max_list_iter_2(self):
        """passes list and checks if max val is correct"""
        l1 = [1, 2, 3]
        self.assertEqual(max_list_iter(l1), 3)

    def test_max_list_iter_3(self):
        """passes empty list and checks if None is returned"""
        l1 = []
        self.assertIsNone(max_list_iter(l1))

    def test_reverse_rec_1(self):
        """passes list and checks if reversed is returned"""
        input_list = [1, 2, 3]
        output = [3, 2, 1]
        self.assertListEqual(reverse_rec(input_list), output)

    def test_reverse_rec_2(self):
        """passes empty list and checks if empty list is returned"""
        output = input_list = []
        self.assertListEqual(reverse_rec(input_list), output)

    def test_reverse_rec_3(self):
        """passes list and checks if reversed list is returned"""
        input_list = [-4, -1, -6]
        output = [-6, -1, -4]
        self.assertListEqual(reverse_rec(input_list), output)

    def test_bin_search_1(self):
        """This test is a standard test for the binary search function"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)

    def test_bin_search_2(self):
        """This tests has low/high on the left of the list"""
        list_val = [0, 1, 2, 3, 4, 5]
        low = 0
        high = 2
        self.assertEqual(bin_search(1, low, high, list_val), 1)

    def test_bin_search_3(self):
        """this test tests valueError functionality"""
        list_val = [0, 1, 2, 3, 4, 5]
        low = 1
        high = 5
        with self.assertRaises(ValueError):
            bin_search(0, low, high, list_val)

    def test_bin_search_4(self):
        """This test has low/high on the right on the list"""
        list_val = [1, 2, 3, 4, 5, 6]
        low = 2
        high = 5
        self.assertEqual(bin_search(4, low, high, list_val), 3)


if __name__ == "__main__":
        unittest.main()

    
