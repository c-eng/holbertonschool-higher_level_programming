#!/usr/bin/python3
"""Unittest for base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Testing class for Base
    """

    def setUp(self):
        """Setup actions
        """
        Base._Base__nb_objects = 0

    def test_base_id(self):
        """Testing id assignment
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(42)
        b4 = Base()
        b5 = Base("Hello")
        b6 = Base((1, ))
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 42)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, "Hello")
        self.assertEqual(b6.id, (1,))
