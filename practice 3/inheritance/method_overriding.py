#here is an example of method overriding
class Person:
    def printname(self):
        print("I am a person")
class Student(Person):
    def printname(self):
        print("I am a student")
x = Student()
x.printname()