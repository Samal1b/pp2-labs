#here is a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#here is a lambda function that checks if a number is prime
is_prime = lambda number: number > 1 and all(number % divisor != 0 for divisor in range(2, int(number ** 0.5) + 1))
#here is the filter function that selects prime numbers
prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)