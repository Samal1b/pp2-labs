import json 
import re

#[{"name" : "Alice", "emp_id": "12TS99000"}, {"name": "Bruce", "emp_id": "ad123"}]

data = json.loads(input())

for student in data:
    pattern = re.compile(r"[A-Z]{2}[0-9]{4}")
    match_result = pattern.match(student["emp_id"])
    if match_result != None:
        print(student["name"])

