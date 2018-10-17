#!/usr/bin/python3
"""Student class
"""


class Student:
    """Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict method
        """
        if attrs is not None:
            new = {}
            for i in list(attrs):
                if i in self.__dict__:
                    new[i] = self.__dict__[i]
            return new
        return self.__dict__

    def reload_from_json(self, json):
        """Dict method
        """
        for k, v in json.items():
            self.__dict__[k] = v
