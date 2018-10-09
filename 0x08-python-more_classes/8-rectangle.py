#!/usr/bin/python3
"""
Documentation for Class Rectangle
"""


class Rectangle:
    """
    Generic Rectangle object
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initilization method for the Rectangle class.

        Args:
            width(int): Width fo Rectangle
            height(int): Height of Rectangle
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """Method for formatted output
        """
        if self.__width and self.__height:
            return ((str(self.print_symbol) * self.__width + '\n') *
                    (self.__height - 1)) + (str(self.print_symbol) *
                                            self.__width)
        else:
            return ""

    def __repr__(self):
        """Method for formatted output
        """
        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    def __del__(self):
        if self.__class__.number_of_instances > 0:
            print("Bye rectangle...")
            self.__class__.number_of_instances -= 1
        else:
            print("Nobody here but us chickens")

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

    def bigger_or_equal(rect_1, rect_2):
        """Method for comparing two Rectangles

        Args:
            rect_1 (:obj: Rectangle): First rectangle to compare
            rect_2 (:obj: Rectangle): Second rectangle to compare
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

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

    @height.setter
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
