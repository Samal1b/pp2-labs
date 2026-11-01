# {"name": "Anna", "email": "anna@gmail.com"},
 # {"name": "Tim", "email": "tim@company"},
#  {"name": "Ali", "email": "ali@mail.kz"},
 # {"name": "Kate", "email": "katemail.com"}
#]

import json 
import re

data=json.loads(input())
pattern=re.compile(r"[A-Za-z0-9]+@[a-z]+\.[A-Za-z{2,}]")

for student in data:
    if pattern.match(student["email"]):
        print(student["name"])
