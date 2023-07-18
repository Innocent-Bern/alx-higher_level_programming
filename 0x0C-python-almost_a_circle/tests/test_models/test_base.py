#!/usr/bin/python3
"""unit test for base.py"""


import unittest
from models.base import Base


class TestBase_Attr__Methods(unittest.TestCase):
    """test base class attributes and methods"""

    def test_blank_id(self):
        self.assertEqual(Base().id, 1)

    def test_assigned_id(self):
        self.assertEqual(Base(5).id, 5)

if __name__ == "__main__":
    unittest.main()
