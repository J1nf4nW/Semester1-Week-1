# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from shapes import Circle, Shape, Point
circle = Circle(2.5, Point(0,0), "red")
print(circle)
print(f"area = {circle.area():.3f}")
print(f"perimeter = {circle.perimeter():.3f}")