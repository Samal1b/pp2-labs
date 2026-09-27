# 1
def squar(n): 
    for i in range(n+1):
        yield i**2


# 2
def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

# for x in even(int(input())):
#     print(x, end=", ")

# 3
def div_by_3_4(n):
    for num in range(n+1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

# for y in div_by_3_4(int(input())):
#     print(y)

# 4
def squar(a, n): 
    for i in range(a, n+1):
        yield i**2

# for x in squar(6, 70):
#     print(x)

# 5
def from_down_to(n):
    for num in range(n,0 - 1,-1):
        yield num

for x in from_down_to(100):
    print(x)


