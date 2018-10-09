#!/usr/bin/python3
"""
Documentation for Class Rectangle
"""

class Rectangle:
    """
    Generic Rectangle object
    """

    def __init__(self, width = 0, height = 0):
        """Initilization method for the Rectangle class.

        Args:
            width(int): Width fo Rectangle
            height(int): Height of Rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """Method for Rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Method for Rectangle perimiter
        """
        if self.__width and self.__height:
            return self.__width * 2 + self.__height * 2
        else:
            return int(0)

    @property
    def width(self):
        """Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):

        """Setter method for width

        Args:
            value(int): Width of Rectangle
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter method for height
        """
        return self.__height

    @width.setter
    def height(self, value):

        """Setter method for height

        Args:
            value(int): Height of Rectangle
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
