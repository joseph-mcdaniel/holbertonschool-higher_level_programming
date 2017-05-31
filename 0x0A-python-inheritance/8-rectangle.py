#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):

        self.__width = width
        self.__height = height
        # integer_validator(name, value) checks if int
        self.integer_validator("width", width)
        self.integer_validator("height", height)
