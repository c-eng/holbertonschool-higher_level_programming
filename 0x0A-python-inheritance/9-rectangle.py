#!/usr/bin/python3
"""Rectangle classe
"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Rectangle class from BaseGeometry class
    """

    def __init__(self, width, height):
        """Initilization of the Rectangle class
        Args:
            width (int): width
            height (int): height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Method for formatted output
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Calculates area
        """
        return self.__width * self.__height
