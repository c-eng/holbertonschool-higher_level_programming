#!/usr/bin/python3
class Square:
    """Generic square object
    """

    def __init__(self, size=0):

        """Initilization method for the Square class. Includes testing
        for input variable

        Args:
            size(int): Size of Square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
