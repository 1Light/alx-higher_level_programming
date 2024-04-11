#!/usr/bin/python3

""" This is a script """


class Square:
    """This is a class"""

    def __init__(self, size=0):
        """This is a method"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            for _ in range(self.__size):
                print("#" * self.__size)
