#!/usr/bin/python3
"""BaseGeometry and Rectangle classes
"""


class BaseGeometry:
    """Base Geometry class for polygons
    """
    def area(self):
        """Calculates area (supposedly) but not yet implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates a value
        Args:
            name (string): a string
            value (int): an int
        """
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Rectangle class from BaseGeometry class
    """

    __width = 1
    __height = 1

    def __init__(self, width, height):
        """Initilizes rectangle
        """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
