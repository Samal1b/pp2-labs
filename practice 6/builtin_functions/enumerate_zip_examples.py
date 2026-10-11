names = ["Alice", "Bob", "Charlie"]
grades = [90, 85, 95]

for index, name in enumerate(names):
    print(index, name)

for name, grade in zip(names, grades):
    print(name, grade)

print(sorted(names))
print(list("Python"))
print(tuple(names))
print(set([1, 2, 2, 3]))

number = "100"
print(int(number))
print(float(number))
print(type(number))