#here is a function that accepts multiple child names and prints the youngest child's name
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")



#here is a function that accepts multiple numbers and calculates their sum.
def calculate_sum(*numbers):
    return sum(numbers)


result = calculate_sum(10, 20, 30, 40)
print("The sum is:", result)



#here is a function that accepts multiple arguments and shows their type, individual values, and all arguments.
def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)


my_function("Emil", "Tobias", "Linus")