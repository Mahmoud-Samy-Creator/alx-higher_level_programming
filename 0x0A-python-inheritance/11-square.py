#!/usr/bin/python3
"""more class base
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
