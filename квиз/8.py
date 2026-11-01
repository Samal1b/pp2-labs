# {"name": "Anna", "email": "anna@gmail.com"},
 # {"name": "Tim", "email": "tim@company"},
#  {"name": "Ali", "email": "ali@mail.kz"},
 # {"name": "Kate", "email": "katemail.com"}
#]

import json 
import re

pattern=re.compile(r"[A-Za-z0-9]+@[A-Za-z]+\.[a-z]{2,}")


data = json.loads(input())

for student in data:
    if pattern.match(student["email"]):
        print(student["name"])