# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate
    # Add distance() method here
    def distance(self):
        return math.hypot(self.x, self.y)
    # Add distance_to() method here
    def distance_to(self, point_2):
        return math.hypot(self.x - point_2.x, self.y - point_2.y)
 # (This will need a parameter representing another point)
# Finally, add code here to demonstrate use of Point
p = Point(1.5,2.0)
print(p.x, p.y)
print(p.distance())

p2 = Point(4.0,6.0)
print(p2.x, p2.y)
print(p.distance_to(p2))