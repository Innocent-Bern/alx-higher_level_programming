#!/usr/bin/python3
"""unit test for base.py"""


import unittest
from models.base import Base


class TestBaseAttrAndMethods(unittest.TestCase):
    """test base class attributes and methods"""

    def test_nb_instances(self):
        inst_a = Base()
        self.assertEqual(inst_a.__nb_objects, 1)

if __name__ == "__main__":
    unittest.main()
