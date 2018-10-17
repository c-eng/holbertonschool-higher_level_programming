#!/usr/bin/python3
"""Square class
"""


class Square(__import__('9-rectangle').Rectangle):
    """Square subclass of Rectangle
    """
    def __init__(self, size):
        """Initilization method
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
