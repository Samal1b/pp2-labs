#here is the Point class
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
#here are two Point objects
first_point = Point(1, 2)
second_point = Point(4, 6)
#here is the code that shows the first point
first_point.show()
#here is the code that calculates the distance
print(first_point.dist(second_point))
