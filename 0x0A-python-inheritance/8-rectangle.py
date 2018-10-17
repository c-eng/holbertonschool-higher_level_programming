#!/usr/bin/python3
"""BaseGeometry and Rectangle classes
"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Rectangle class from BaseGeometry class
    """

    def __init__(self, width, height):
        """Initilizes rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
