#!/usr/bin/python3
"""Square class to define a square"""


class Square:
    """Initializing values"""
    def __init__(self, size=0):
        '''Creatign a private attribute'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        '''A function return area of square'''
        return (self.__size * self.__size)
