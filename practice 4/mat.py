import math


radians=math.radians(15)
print(radians)

#2
def area_trap(a,b,h):
    return(((a+b)*h)/2)
print(area_trap(5,6,5))

#3
def area(n,a):
    return(((n*a*a)/4) * (1/math.tan(math.radians(180/n))))

print(area(4,25))


#4
def paral(a,h):
    return(a*h)

print(paral(5,6))