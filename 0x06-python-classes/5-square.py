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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for i in range(0, self.__size):
                    print("#", end="")
                print("")
