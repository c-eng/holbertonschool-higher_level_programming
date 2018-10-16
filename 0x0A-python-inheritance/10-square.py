#!/usr/bin/python3
"""Square class
"""


class Square(__import__('9-rectangle').Rectangle):
    """Square subclass of Rectangle
    """
    def __init__(self, size):
        """Initilization method
        """
        super().__init__(size, size)
