import os

path = "."

print("Directories:")
for x in os.listdir(path):
    if os.path.isdir(os.path.join(path, x)):
        print(x)

print("Files:")
for x in os.listdir(path):
    if os.path.isfile(os.path.join(path, x)):
        print(x)

print("All:")
print(os.listdir(path))