#!/usr/bin/python3
"""Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Init method
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Update method
        """
        if args:
            for i in range(len(args)):
                if i is 0:
                    self.id = args[i]
                if i is 1:
                    self.width = args[i]
                    self.height = args[i]
                if i is 2:
                    self.x = args[i]
                if i is 3:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "size":
                    self.width = kwargs[key]
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
        out = {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.width}
        return out

    @property
    def size(self):
        """Getter method
        """
        return super().width

    @size.setter
    def size(self, value):
        """Setter method
        """
        self.width = value
        self.height = value
