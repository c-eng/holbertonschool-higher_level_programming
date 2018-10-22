#!/usr/bin/python3
"""Base Class
"""
import json


class Base:
    """Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initilization method
        Args:
            id (int?): id of base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON serialization method
        """
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON serialization to file method
        """
        lst = []
        if list_objs:
            for i in list_objs:
                lst.append(i.to_dictionary())
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """JSON deserialization method
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Creates an object
        """
        if cls.__name__ == 'Rectangle':
            temp = cls(1, 1)
        elif cls.__name__ == 'Square':
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """JSON deserialization from file method
        """
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                temp = []
                lst = cls.from_json_string(f.read())
                for i in lst:
                    temp.append(cls.create(**i))
                return temp
        except FileNotFoundError:
            return []
