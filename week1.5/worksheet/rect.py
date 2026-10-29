# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        if not isinstance(width, (int,float)):
            raise TypeError("width must be an integer")
        if width <= 0:        
            raise ValueError("width must be greater than 0")
        if not isinstance(height, (int,float)):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be greater than 0")
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height
    def is_square(self):
           """
           Checks if the Rectangle's given width and height are the same.
           """
           if self.width == self.height:
                  return True
           else:
                  return False
    def area(self):
           """
           Returns the Rectangle's area by using width * height.
           """
           return self.width * self.height
    def perimeter(self):
           """
           Returns the Rectangle's perimeter by using 2*(width * height).
           """
           return 2 * (self.width + self.height)

r = Rectangle(5,0)
print(r.is_square())
print(r.area())
print(r.perimeter())


    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
