#!/usr/bin/python3
"""This module defines a Square class"""


class square():
    """Square class definition"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Constructor for squeare instances"""
        for key, value in kwargs.items():
            setattr(self, key, value)

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
