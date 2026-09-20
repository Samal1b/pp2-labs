#here is the String class
class String:
    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())


# Here is an object that gets and prints the string
string_object = String()
string_object.getString()
string_object.printString()
