import os

if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("File deleted")
else:
    print("File not found")