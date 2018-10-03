#!/usr/bin/python3
class Square:
    """Generic square object
    """

    def __init__(self, size=0):
        """Initilization method for the Square class.

        Args:
            size(int): Size of Square
        """
        self.size = size

    def area(self):
        """Area calculation for Square object, takes no arguments
        """
        return self.__size ** 2

    def my_print(self):
        """Prints representation of Square with '#' character
        """
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size is 0:
            print()

    @property
    def size(self):
        """Getter method for Square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for Square size

        Args:
            value (int): Value of Square size
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
