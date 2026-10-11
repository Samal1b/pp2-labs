def even(n):
    for num in range(0,n+1):
        if num%2==0:
            yield num

print(even(6))


