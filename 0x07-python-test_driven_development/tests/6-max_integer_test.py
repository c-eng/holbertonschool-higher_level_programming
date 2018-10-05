#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Testing class for unit testing
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([-1, 2, 4, 3]), 4)

    def test_max_integer_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer_str(self):
        with self.assertRaises(TypeError):
            max_integer([1, "hi", 3, 4])
