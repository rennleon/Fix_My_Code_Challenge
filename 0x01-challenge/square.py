#!/usr/bin/python3
"""This module defines a Square class"""


class square():
    """Square class definition"""

    def __init__(self, width, height):
        """Constructor for squeare instances"""
        self.width = width
        self.height = height

    def __validate(self, value):
        """Data validation for edges"""
        if type(value) is not int:
            raise TypeError('Value must be an integer')
        if value <= 0:
            raise ValueError('Value must be greater than zero')

    @property
    def width(self):
        """Width proerty method"""
        return self.__width

    @width.setter
    def width(self, value):
        """"Width property setter"""
        self.__validate(value)
        self.__width = value

    @property
    def height(self):
        """Width proerty method"""
        return self.__height

    @height.setter
    def height(self, value):
        """"Height property setter"""
        self.__validate(value)
        self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Perimeter of the Sqaure"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
