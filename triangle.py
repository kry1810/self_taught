class Triangle:
    def __init__(self, l, h):
        self.length = l
        self.height = h

    def area(self):
        return self.length * self.height / 2

triangle = Triangle(4, 3)
print (triangle.area())