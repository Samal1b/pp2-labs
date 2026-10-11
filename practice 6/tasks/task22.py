import os

path = input("Enter filename: ")

if os.path.exists(path) and os.path.isfile(path):
    if os.access(path, os.W_OK):
        answer = input("Delete file? yes/no: ")

        if answer == "yes":
            os.remove(path)
            print("File deleted")
        else:
            print("Cancelled")
    else:
        print("No write access")
else:
    print("File not found")