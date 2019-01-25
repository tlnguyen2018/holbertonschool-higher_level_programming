#!/usr/bin/python3
"""
Unittest for Rectangle
"""

from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_no_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 1)
        r4 = Rectangle(1, 1, 0, 0)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r4.id, 4)

    def text_with_id_and_mix(self):
        r5 = Rectangle(10, 2, 1, 1, 100)
        r6 = Rectangle(2, 10, 1, 1, -100)
        r7 = Rectangle(10, 2, 1, 1)
        r8 = Rectangle(10, 3, 1, 1)
        r9 = Rectangle(10, 2, 1, 1, 3.14)
        r10 = Rectangle(10, 2, 1, 1, "Hello")
        self.assertEqual(r5.id, 100)
        self.assertEqual(r6.id, -100)
        self.assertEqual(r7.id, r4.id + 1)
        self.assertEqual(r8.id, r7.id + 1)
        self.assertEqual(r9.id, 3.14)
        self.assertEqual(r10.id, "Hello")
