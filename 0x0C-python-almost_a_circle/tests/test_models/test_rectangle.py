#!/usr/bin/python3
"""Unittest for rectangle.py
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Testing class for Rectangle
    """
    def setUp(self):
        """Setup actions
        """
        Base._Base__nb_objects = 0

    def test_id(self):
        """Testing id setting
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(1, 1, 1, 1, "Bella")
        self.assertEqual(r4.id, "Bella")

    def test_values(self):
        """Testing input validation
        """
        r4 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r4.x = {}
        with self.assertRaises(TypeError):
            r4.y = True
        with self.assertRaises(TypeError):
            r4.height = True
        with self.assertRaises(TypeError):
            r5 = Rectangle("2", 10)
        r6 = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r6.width = -10
        with self.assertRaises(ValueError):
            r6.height = -10
        with self.assertRaises(ValueError):
            r6.y = -3
        with self.assertRaises(ValueError):
            r6.x = -3
        with self.assertRaises(ValueError):
            r6.width = 0
        with self.assertRaises(ValueError):
            r6.height = 0
        with self.assertRaises(TypeError):
            r7 = Rectangle()
        with self.assertRaises(TypeError):
            r8 = Rectangle(3.14159, 1)
        with self.assertRaises(TypeError):
            r9 = Rectangle(3, 1.41421)
        with self.assertRaises(TypeError):
            r10 = Rectangle(3, 1, 3.14159, 1)
        with self.assertRaises(TypeError):
            r11 = Rectangle(3, 1, 3, 1.41421)

    def test_area(self):
        """Testing area
        """
        r8 = Rectangle(3, 2)
        self.assertEqual(r8.area(), 6)
        r9 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r9.area(), 56)


    def test_display(self):
        """Testing display
        """
        r1 = Rectangle(4, 6)
        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        r1.display()
        self.assertEqual(capturedOutput1.getvalue(),
                         "####\n####\n####\n####\n####\n####\n")
        r2 = Rectangle(2, 3, 2, 2)
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        r2.display()
        self.assertEqual(capturedOutput2.getvalue(),
                         "\n\n  ##\n  ##\n  ##\n")
        r3 = Rectangle(2, 3, 0, 2)
        capturedOutput3 = io.StringIO()
        sys.stdout = capturedOutput3
        r3.display()
        self.assertEqual(capturedOutput3.getvalue(),
                         "\n\n##\n##\n##\n")
        r4 = Rectangle(2, 3, 2, 0)
        capturedOutput4 = io.StringIO()
        sys.stdout = capturedOutput4
        r4.display()
        self.assertEqual(capturedOutput4.getvalue(),
                         "  ##\n  ##\n  ##\n")
        sys.stdout = sys.__stdout__

    def test_print(self):
        """Testing print
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        print(r1)
        self.assertEqual(capturedOutput1.getvalue(),
                         "[Rectangle] (12) 2/1 - 4/6\n")
        r2 = Rectangle(5, 5, 1)
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        print(r2)
        self.assertEqual(capturedOutput2.getvalue(),
                         "[Rectangle] (1) 1/0 - 5/5\n")
        sys.stdout = sys.__stdout__

    def test_update(self):
        """Testing update
        """
        r1 = Rectangle(10, 10, 10, 10)
        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        print(r1)
        self.assertEqual(capturedOutput1.getvalue(),
                         "[Rectangle] (1) 10/10 - 10/10\n")
        r1.update(89, 2, 3, 4, 5)
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        print(r1)
        self.assertEqual(capturedOutput2.getvalue(),
                         "[Rectangle] (89) 4/5 - 2/3\n")
        r1.update()
        capturedOutput3 = io.StringIO()
        sys.stdout = capturedOutput3
        print(r1)
        self.assertEqual(capturedOutput3.getvalue(),
                         "[Rectangle] (89) 4/5 - 2/3\n")
        r1.update(y=1, width=4, x=3, id=88)
        capturedOutput4 = io.StringIO()
        sys.stdout = capturedOutput4
        print(r1)
        self.assertEqual(capturedOutput4.getvalue(),
                         "[Rectangle] (88) 3/1 - 4/3\n")
        r1.update(x=1, height=4, y=3, width=2)
        capturedOutput5 = io.StringIO()
        sys.stdout = capturedOutput5
        print(r1)
        self.assertEqual(capturedOutput5.getvalue(),
                         "[Rectangle] (88) 1/3 - 2/4\n")

        sys.stdout = sys.__stdout__

    def test_dict(self):
        """Testing to_dict
        """
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 9, 'id': 1,
                                              'height': 2, 'width': 10})
        self.assertEqual(type(r1.to_dictionary()), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r2.to_dictionary(), {'x': 1, 'y': 9, 'id': 1,
                                              'height': 2, 'width': 10})
        self.assertNotEqual(r1, r2)

    def test_json(self):
        """Testing json
        """
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r1.to_dictionary(), {'x': 2, 'width': 10, 'id': 1,
                                              'height': 7, 'y': 8})
        json = Base.to_json_string([r1.to_dictionary()])
        self.assertEqual(type(json), str)
