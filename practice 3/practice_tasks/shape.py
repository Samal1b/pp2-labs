#here is the Shape class
class Shape:
    def area(self):
        print(0)
#here is the Square class that inherits from Shape
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)
#here is an object of the Square class
square_object = Square(int(input()))
square_object.area()
