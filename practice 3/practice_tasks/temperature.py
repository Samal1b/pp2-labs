#here is a function that converts Fahrenheit to Celsius
def fahrenheittocelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)
fahrenheit = float(input("Enter Fahrenheit: "))
print(fahrenheittocelsius(fahrenheit))