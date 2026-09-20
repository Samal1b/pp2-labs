#here is a filter function that uses lambda to select only odd numbers from the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers)


#here is a filter function that uses lambda to select numbers greater than 5.
numbers = [2, 4, 6, 7, 9, 10, 12]
large_numbers = list(filter(lambda x: x > 5, numbers))

print(large_numbers)