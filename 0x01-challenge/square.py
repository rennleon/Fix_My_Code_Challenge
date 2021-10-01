#!/usr/bin/python3
"""This module defines a Square class"""


class square():
    """Square class definition"""

    def __init__(self, *args, **kwargs):
        """Constructor for squeare instances"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def size(self):
        """Width proerty method"""
        return self.__size

    @size.setter
    def size(self, value):
        """"Width property setter"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value <= 0:
            raise ValueError('size must be greater than zero')
        self.__size = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.size ** 2

    def perimeter_of_my_square(self):
        """Perimeter of the Sqaure"""
        return self.size * 4

    def __str__(self):
        """String representation of the square"""
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":
    s = square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
