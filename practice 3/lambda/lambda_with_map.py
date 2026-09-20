#here is a map function that uses lambda to double every number in the list.
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)


#here is a map function that uses lambda to convert temperatures from celsius to fahrenheit.
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda x: x * 9 / 5 + 32, celsius))

print(fahrenheit)