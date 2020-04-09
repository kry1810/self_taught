import math

class Circle:
    def __init__(self, d):
        self.diameter = d

    def area(self):
        return self.diameter ** 2  * math.pi / 4

circle = Circle(20)
print(circle.area())