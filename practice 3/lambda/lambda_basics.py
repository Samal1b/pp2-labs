#here is a lambda function that takes three numbers and returns their sum.
x = lambda a, b, c:a + b + c
print(x(5, 6, 2))


#here is a function that uses a lambda expression to calculate the square of a number.
def calculate_square(number):
    square = lambda x: x * x
    return square(number)


print(calculate_square(5))
print(calculate_square(8))