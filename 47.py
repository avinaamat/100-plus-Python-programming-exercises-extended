# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
#
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(math.pi*self.radius**2)

a= Circle(5.24)
a.area()