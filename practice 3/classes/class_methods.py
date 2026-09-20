#here is a class with a method that greets the person using their name.
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()