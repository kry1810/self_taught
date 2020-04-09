class Shape():
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, l, w):
        self.len = l
        self.width = w

    def calculate_perimeter(self):
        return self.len * 2 + self.width * 2

my_rectangle = Rectangle(20, 40)
print(my_rectangle.calculate_perimeter())

my_rectangle.what_am_i()

class Square(Shape):
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return  self.len * 4

    def change_size(self, l2):
        self.len += l2

my_square = Square(100)
print (my_square.len)

my_square2 = (my_square.change_size(200))
print (my_square.len)

my_square.what_am_i()


