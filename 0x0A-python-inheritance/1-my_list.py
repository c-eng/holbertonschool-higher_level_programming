#!/usr/bin/python3
"""MyList class object
"""


class MyList(list):
    """MyList class with custom methods
    """

    def print_sorted(self):
        print(sorted(self))
