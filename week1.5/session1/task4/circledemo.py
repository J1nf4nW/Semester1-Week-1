# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
from geometry import Point, Circle
x = float(input("Enter the x coordinate of the circle's centre:"))
y = float(input("Enter the y coordinate of the circle's centre:"))
centre_point = Point(x,y)
radius_val = float(input("Enter the length of the radius in the circle:"))
input_circle = Circle(centre_point,radius_val)

print(f"The area of the circle is {input_circle.area():4f}")
print(f"The perimeter of the circle is {input_circle.perimeter():4f}")