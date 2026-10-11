f = open("practice.txt", "w")
f.write("Hello! Welcome to practice.txt")
f.close()

f = open("practice.txt", "r")
print(f.read())
f.close()

f = open("practice.txt", "r")
print(f.read(5))
f.close()

f = open("practice.txt", "r")
print(f.readline())
f.close()

f = open("practice.txt", "r")
for x in f:
    print(x)
f.close()