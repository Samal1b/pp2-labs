import json


with open("./data.json") as file:
    data = json.load(file)
    # data = json.loads(input())

    # for student in data:
    #     if student["active"]:
    #         print(student["name"])
        
    # for student in data:
    #     if student["major"] == "IT":
    #         print(student["name"])

    # for student in data:
    #     if student["gpa"]>=3.5:
    #         print(student["gpa"], student["name"])

    for student in data:
        student_avg_grade = sum(student["grades"]) / len(student["grades"])
        print(student["name"], round(student_avg_grade))