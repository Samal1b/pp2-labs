#here is a class that uses the __init__ method to set the name and age of an object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)