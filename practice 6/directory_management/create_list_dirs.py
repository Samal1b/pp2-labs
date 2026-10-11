import os

os.makedirs("practice/folder", exist_ok=True)

print(os.getcwd())
print(os.listdir("practice"))

for root, dirs, files in os.walk("practice"):
    print("Directories:", dirs)
    print("Files:", files)

path = "practice"

print(os.path.exists(path))
print(os.path.isdir(path))
print(os.path.isfile(path))