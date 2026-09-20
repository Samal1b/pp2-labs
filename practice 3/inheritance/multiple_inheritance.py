#here is an example of multiple inheritance
class A:
    def hello(self):
        print("Hello")

class B:
    def bye(self):
        print("Bye")

class C(A, B):
    pass

x = C()
x.hello()
x.bye()