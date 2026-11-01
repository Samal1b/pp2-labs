def quads_gen(n):
    for i in range(n + 1):
        yield i ** 2


n = 10

for num in quads_gen(n):
    print(num)