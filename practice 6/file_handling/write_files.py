f = open("practice.txt", "w")
f.write("Hello! Welcome to practice.txt")
f.close()

f = open("practice.txt", "a")
f.write("\nThis is additional content.")
f.close()

f = open("practice.txt", "r")
print(f.read())
f.close()

f = open("practice2.txt", "x")
f.write("This is a new file.")
f.close()