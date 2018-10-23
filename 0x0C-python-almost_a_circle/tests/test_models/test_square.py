#!/usr/bin/python3
"""Unittest for square.py
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Testing class for Square
    """
    def setUp(self):
        """Setup actions
        """
        Base._Base__nb_objects = 0

    def test_init(self):
        """Testing init
        """
        s1 = Square(5)
        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        print(s1)
        print(s1.area())
        s1.display()
        self.assertEqual(capturedOutput1.getvalue(),
                         "[Square] (1) 0/0 - 5\n25\n#####\n#####\n#####\n"
                         "#####\n#####\n")
        s2 = Square(2, 2)
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        print(s2)
        print(s2.area())
        s2.display()
        self.assertEqual(capturedOutput2.getvalue(),
                         "[Square] (2) 2/0 - 2\n4\n  ##\n  ##\n")
        s3 = Square(3, 1, 3)
        capturedOutput3 = io.StringIO()
        sys.stdout = capturedOutput3
        print(s3)
        print(s3.area())
        s3.display()
        self.assertEqual(capturedOutput3.getvalue(),
                         "[Square] (3) 1/3 - 3\n9\n\n\n\n ###\n ###\n ###\n")
        sys.stdout = sys.__stdout__
        with self.assertRaises(TypeError):
            s4 = Square()

    def test_get_set(self):
        """Testing getting/setting
        """
        s1 = Square(10, 9, 8)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 9)
        self.assertEqual(s1.y, 8)
        s1.height = 7
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.height, 7)
        with self.assertRaises(TypeError):
            s1.size = "9"
        with self.assertRaises(TypeError):
            s1.x = {}
        with self.assertRaises(TypeError):
            s1.y = 3.14159
        with self.assertRaises(TypeError):
            s1.size = True
        with self.assertRaises(TypeError):
            s1.x = True
        with self.assertRaises(TypeError):
            s1.y = True
        with self.assertRaises(TypeError):
            s2 = Square("eleventeen")
        with self.assertRaises(ValueError):
            s1.size = 0
        with self.assertRaises(ValueError):
            s1.size = -5
        with self.assertRaises(ValueError):
            s1.x = -3
        with self.assertRaises(ValueError):
            s1.y = -3
        with self.assertRaises(TypeError):
            s2 = Square()


    def test_update(self):
        """Testing updating
        """
        s1 = Square(5)
        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        print(s1)
        s1.update(10, 2)
        print(s1)
        s1.update(1, 2, 3, 4, 5)
        print(s1)
        s1.update()
        print(s1)
        self.assertEqual(capturedOutput1.getvalue(),
                         "[Square] (1) 0/0 - 5\n[Square] (10) 0/0 - 2\n"
                         "[Square] (1) 3/4 - 2\n[Square] (1) 3/4 - 2\n")
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        s1.update(x=12)
        print(s1)
        s1.update(size=7, id=89, y=1, z=999)
        print(s1)
        s1.update(zxy=123)
        print(s1)
        self.assertEqual(capturedOutput2.getvalue(),
                         "[Square] (1) 12/4 - 2\n[Square] (89) 12/1 - 7\n"
                         "[Square] (89) 12/1 - 7\n")
        sys.stdout = sys.__stdout__
        with self.assertRaises(TypeError):
            s1.update("Mello", "Yellow")
        with self.assertRaises(TypeError):
            s1.update(1, 2, {}, 4)
        with self.assertRaises(TypeError):
            s1.update(1, 2, 3, True)
        with self.assertRaises(ValueError):
            s1.update("Negative one", -1)
        with self.assertRaises(ValueError):
            s1.update(size=0)
        with self.assertRaises(ValueError):
            s1.update(1, 2, -3, 4)
        with self.assertRaises(ValueError):
            s1.update(y=-4)

    def test_dict(self):
        """Testing to_dict
        """
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'x': 2, 'size': 10,
                                              'y': 1})
        self.assertEqual(type(s1.to_dictionary()), dict)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(s2.to_dictionary(), {'id': 1, 'x': 2, 'size': 10,
                                              'y': 1})
        self.assertNotEqual(s1, s2)

    def test_json(self):
        """Testing json
        """
        s1 = Square(5)
        json = Base.to_json_string([s1.to_dictionary()])
        self.assertEqual(type(json), str)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        with open("Square.json", "r") as file:
            self.assertEqual(type(file.read()), str)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        for square in list_squares_input:
            print(square)
        for square in list_squares_output:
            print(square)
        self.assertEqual(capturedOutput2.getvalue(),
                          "[Square] (1) 0/0 - 5\n"
                          "[Square] (2) 9/1 - 7\n"
                          "[Square] (1) 0/0 - 5\n"
                          "[Square] (2) 9/1 - 7\n")
        self.assertNotEqual(id(list_squares_input[0]),
                            id(list_squares_output[0]))
        self.assertNotEqual(id(list_squares_input[1]),
                            id(list_squares_output[1]))
        sys.stdout = sys.__stdout__

    def test_csv(self):
        """Testing csv
        """
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        for square in list_squares_input:
            print(square)
        for square in list_squares_output:
            print(square)
        self.assertEqual(capturedOutput.getvalue(),
                          "[Square] (1) 0/0 - 5\n"
                          "[Square] (2) 9/1 - 7\n"
                          "[Square] (1) 0/0 - 5\n"
                          "[Square] (2) 9/1 - 7\n")
        sys.stdout = sys.__stdout__
        self.assertNotEqual(id(list_squares_input[0]),
                            id(list_squares_output[0]))
        self.assertNotEqual(id(list_squares_input[1]),
                            id(list_squares_output[1]))
