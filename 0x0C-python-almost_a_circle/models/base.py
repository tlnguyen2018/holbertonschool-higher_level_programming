#!/usr/bin/python3
"""
Create file base.py
Create class Base
"""


class Base:
    """
    private attribute __nb_objects = 0
    """
    __nb_objects = 0
    """
    class constructor
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            """
            Assign new value to id
            """
            self.id = Base.__nb_objects
