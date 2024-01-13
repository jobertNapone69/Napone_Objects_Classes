import math

class Circle:
 def __init__(self, radius):
       """Initializes the circle with the given radius."""
       self.radius = radius

 def area(self):
       """Calculates and prints the area of the circle."""
       area = math.pi * self.radius**2
       print(f"The area of the circle is: {area:.2f}")

 def perimeter(self):
       """Calculates and prints the perimeter of the circle."""
       perimeter = 2 * math.pi * self.radius
       print(f"The perimeter of the circle is: {perimeter:.2f}")

# Create a circle object with radius 5
circle = Circle(69)

# Call the area and perimeter methods
circle.area()
circle.perimeter()
