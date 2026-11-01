import re 
import json 

data=json.loads(input())

pattern=re.compile(r"^[A-Za-z0-9]+@[A-Za-z]+\.[a-z]{2,}")
for student in data:
    if pattern.match(student["email"]):
        print(student["name"])