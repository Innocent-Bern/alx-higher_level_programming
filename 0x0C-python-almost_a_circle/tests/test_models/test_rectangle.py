#!/usr/bin/python3
"""test module for rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle_Attributes_Methods(unittest.TestCase):
    """test rectangle class attributes and methods"""

    def test_init_method(self):
        case_a = Rectangle(3, 4, 1, 2)
        self.assertEqual(case_a.width, 3)
        self.assertEqual(case_a.height, 4)
        self.assertEqual(case_a.x, 1)
        self.assertEqual(case_a.y, 2)

    """test __init__ method"""
    """test width getter"""
    """test width setter"""
    """test height getter"""
    """test height setter"""
    """test x getter"""
    """test x setter"""
    """test y getter"""
    """test y setter"""
    """test area method"""
    """test __str__ method"""
    """test update method"""


if __name__ == "__main__":
    unittest.main()
