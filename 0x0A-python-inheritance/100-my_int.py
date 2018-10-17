#!/usr/bin/python3
"""myint
"""


class MyInt(int):
    """myint
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
