import math

x1,y1=map(int, input().split())
x2,y2=map(int, input().split())
x3,y3=map(int, input().split())

ab=math.sqrt((x2-x1)**2+(y2-y1)**2)
ac=math.sqrt((x3-x1)**2+(y3-y1)**2)
bc=math.sqrt((x3-x2)**2+(y3-y2)**2)

print(ab+ac+bc)

