#here is a function that prints all permutations of a string
from itertools import permutations
def print_permutations(text):
    for permutation in permutations(text):
        print((permutation))
#here is an example
text=input("enter a string: ")
print_permutations(text)