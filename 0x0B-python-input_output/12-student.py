#!/usr/bin/python3
"""
class student
like task 11, adding attribute presentation condition
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Check if attr is list, not return everything
        """
        if isinstance(attrs, list):
            for items in attrs:
                if not isinstance(items, str):
                    return self.__dict__
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__
