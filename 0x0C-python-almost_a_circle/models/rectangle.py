#!/usr/bin/python3
"""Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method
        Args:
            width (int?): width of rectangle
            height (int?): height of rectangle
            x (int?): x position
            y (int?): y position
            id (int?): id of object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Area method
        """
        return self.__width * self.__height

    def display(self):
        """Display method
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """print method
        """
        if self.__class__.__name__ == "Square":
                    return '[{}] ({}) {}/{} - {}'.format(
                        self.__class__.__name__, self.id, self.__x, self.__y,
                        self.__width)
        return '[{}] ({}) {}/{} - {}/{}'.format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update method
        """
        if args:
            for i in range(len(args)):
                if i is 0:
                    self.id = args[i]
                if i is 1:
                    self.width = args[i]
                if i is 2:
                    self.height = args[i]
                if i is 3:
                    self.x = args[i]
                if i is 4:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "width":
                    self.width = kwargs[key]
                if key == "height":
                    self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]
                if key == "id":
                    self.id = kwargs[key]

    def to_dictionary(self):
        """Dictionary method
        """
        out = {'x': self.x, 'y': self.y, 'id': self.id, 'width': self.width,
               'height': self.height}
        return out

    @property
    def width(self):
        """Getter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Getter Method
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter Method
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Getter method
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter Method
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
