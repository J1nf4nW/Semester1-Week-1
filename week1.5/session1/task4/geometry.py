# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""
import math

class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    def distance(self):
        return math.hypot(self.x, self.y)

    def distance_to(self, point_2):
        return math.hypot(self.x - point_2.x, self.y - point_2.y)

# Copy Point class definition here

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius
# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
