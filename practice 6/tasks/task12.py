names = ["Ali", "Sara", "John"]
marks = [80, 90, 75]

for i, name in enumerate(names):
    print(i, name)

for name, mark in zip(names, marks):
    print(name, mark)