#!/usr/bin/python3
"""
Unittest for Base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_when_0_base(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_when_have_value_base(self):
        b1 = Base(-10)
        b2 = Base(21)
        b3 = Base("Hello World")
        self.assertEqual(b1.id, -10)
        self.assertEqual(b2.id, 21)
        self.assertEqual(b3.id, "Hello World")
