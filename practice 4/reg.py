import re

receip = "17$ milk, 25$ eggs, 12$ fruits"
pattern=re.compile(r"(\d+\$) (\w+)")

for price, item in pattern.findall(receip):
    print(price)