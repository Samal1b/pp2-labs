#here is a sorted function that uses lambda to sort students by their age.
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)



# here is a sorted function that uses lambda to sort products by their price.
products = [("Laptop", 1200), ("Phone", 800), ("Tablet", 500)]
sorted_products = sorted(products, key=lambda x: x[1])

print(sorted_products)