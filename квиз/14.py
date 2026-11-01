from datetime import datetime

d1=datetime.strptime(input(), "%Y-%m-%d")
d2=datetime.strptime(input(), "%Y-%m-%d")
d3=datetime.strptime(input(), "%Y-%m-%d")
d4=datetime.strptime(input(), "%Y-%m-%d")

print((d2-d1).days)
print((d3-d1).days)
print((d4-d1).days)


