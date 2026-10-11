from functools import reduce

numbers = [1, 2, 3, 4, 5]

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(sorted(numbers))

print(list(map(lambda x: x * 2, numbers)))
print(list(filter(lambda x: x > 2, numbers)))

print(reduce(lambda x, y: x + y, numbers))

value = "10"
print(type(value))
print(int(value))
print(float(value))
print(str(10))
