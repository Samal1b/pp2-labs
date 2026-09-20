#here is a function that checks if a number is prime
def is_prime(number):
    if number < 2:
        return False

    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
#here is a function that filters prime numbers
def filter_prime(numbers):
    return [number for number in numbers if is_prime(number)]
numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(numbers))