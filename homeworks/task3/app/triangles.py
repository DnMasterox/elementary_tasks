__author__ = 'nshumakov'

import math


class Triangle(object):
    def __init__(self, name, a_side, b_side, c_side):
        self.__name = name
        self.__a_side = a_side
        self.__b_side = b_side
        self.__c_side = c_side
        self.__area = 0

    def get_area(self):
        return self.__area

    def calculate_area(self):
        half_perimeter = self.__half_perimeter_of_triangle()
        self.__area = math.sqrt(
            half_perimeter * (half_perimeter - self.__a_side) *
            (half_perimeter - self.__b_side) * (half_perimeter -
                                                self.__c_side))
        return self.__area

    def __half_perimeter_of_triangle(self):
        return (self.__a_side + self.__b_side + self.__c_side) / 2

    def to_print(self):
        print("[Triangle " + self.__name + "]: " + str(round(self.__area, 2))
              + " cm")
