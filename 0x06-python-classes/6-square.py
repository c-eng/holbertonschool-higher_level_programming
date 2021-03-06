#!/usr/bin/python3
class Square:
    """Generic square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initilization method for the Square class.

        Args:
            size (int): Size of Square
            position (:obj:'tuple' of :obj:'int'): Position of Square
        """
        self.size = size
        self.position = position

    def area(self):
        """Area calculation for Square object, takes no arguments
        """
        return self.__size ** 2

    def my_print(self):
        """Prints representation of Square with '#' character.
        Also takes into consideration position in the positive direction
        """
        if self.__size > 0:
            x_pos, y_pos = self.__position
            for i in range(y_pos):
                print()
            for i in range(self.__size):
                print(" " * x_pos, end='')
                print("#" * self.__size)
        else:
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

    @property
    def position(self):
        """Getter method for Square position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for Square position
        Only takes into account positive x, y

        Args:
            value (:obj:'tuple' of :obj:'int'): Position value of Square
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x_pos, y_pos = value
        if not (isinstance(x_pos, int) and isinstance(y_pos, int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if x_pos < 0 or y_pos < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = (x_pos, y_pos)
