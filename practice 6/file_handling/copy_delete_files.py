import os
import shutil

f = open("practice.txt", "w")
f.write("This is a practice file.")
f.close()

shutil.copy("practice.txt", "practice_copy.txt")

if os.path.exists("practice_copy.txt"):
    print("The file exists.")

if os.path.exists("practice_copy.txt"):
    os.remove("practice_copy.txt")

if os.path.exists("practice.txt"):
    print("The original file still exists.")