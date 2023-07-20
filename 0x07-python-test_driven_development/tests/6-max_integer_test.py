#!/usr/bin/python3
"""test module for 6-max_integer.py"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test class"""

    def test_correct_output(self):
        """test correct output"""
        self.assertEqual(max_integer([1, 3, 4]), 4)

    def test_empty_list(self):
        """test empty list"""
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
