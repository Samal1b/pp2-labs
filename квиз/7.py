from datetime import datetime 

d1= datetime.strptime(input(),"%d-%m-%Y")
d2=datetime.strptime(input(),"%d-%m-%Y")
d3=datetime.strptime(input(),"%d-%m-%Y")
d4=datetime.strptime(input(),"%d-%m-%Y")

print((d2-d1).days)
print((d3-d1).days)
print((d4-d1).days)
