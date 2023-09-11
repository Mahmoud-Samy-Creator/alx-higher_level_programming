#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Rectangle a rectangle
    '''
    def __init__(self, width, heihgt):
        self.integer_validator("width", width)
        self.integer_validator("height", heihgt)

        self.__width = width
        self.__heihgt = heihgt
