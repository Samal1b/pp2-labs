#here is the Shape class
class Shape:
    def area(self):
        print(0)
#here is the Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)
#here is an object of the Rectangle class
rectangle_object = Rectangle(int(input()), int(input()))
rectangle_object.area()

