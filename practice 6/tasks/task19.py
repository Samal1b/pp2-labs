fruits = ["Apple", "Banana", "Orange"]

f = open("fruits.txt", "w")

for fruit in fruits:
    f.write(fruit + "\n")

f.close()