#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):

        self.__width = width
        self.__height = height
        # integer_validator(name, value) checks if int
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        # return area
        return self.__width * self.__height

    def __str__(self):
        # return string format to be printed
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
