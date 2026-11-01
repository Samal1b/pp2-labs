from datetime import datetime


# 2026-01-01
# 15-01-2026 01-02-2026 01-03-2026

first_date_str = "01-01-2026"
first_date: datetime = datetime.strptime(first_date_str, "%d-%m-%Y")

date_list_str = input().split(" ")
date_list: list[datetime] = []

for i in range(3):
    date_list.append(datetime.strptime(date_list_str[i], "%d-%m-%Y"))

    print((date_list[i] - first_date).days // 7)