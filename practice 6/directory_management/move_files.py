import os
import shutil

os.makedirs("practice/source", exist_ok=True)
os.makedirs("practice/destination", exist_ok=True)

f = open("practice/source/practice.txt", "w")
f.write("Practice file")
f.close()

shutil.copy(
    "practice/source/practice.txt",
    "practice/destination/practice.txt"
)

shutil.move(
    "practice/source/practice.txt",
    "practice/destination/practice_moved.txt"
)

print(os.listdir("practice/destination"))