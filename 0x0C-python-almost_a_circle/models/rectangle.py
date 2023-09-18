#!/usr/bin/python3

from models.base import Base
import json

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.height * self.width

    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(0, self.y):
            print("")
        for i in range(0, self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            order = 0
            for arg in args:
                if order == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                if order == 1:
                    self.width = arg
                if order == 2:
                    self.height = arg
                if order == 3:
                    self.x = arg
                if order == 4:
                    self.y = arg
                order += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                        self.y = v

    def to_dictionary(self):
        return {
            "id" : self.id,
            "width" : self.width,
            "height" : self.height,
            "x" : self.x,
            "y" : self.y
        }
