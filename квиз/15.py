import math 

rise,run=map(float,input().split())
angle=math.atan(rise/run)
print(math.degrees(angle))