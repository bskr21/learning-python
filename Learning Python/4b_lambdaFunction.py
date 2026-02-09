# Learn how to use Lambda to create a more simple function
# Lambda is anonymous functions that can have any number of arguments  but only one expression
# Lambda used for a simple short operation

# Regular def function
def square(x):
    return x ** 2
print(square(3))

# Change with lambda
# lambda [arguments]: [expression]
square_lambda = lambda x: x ** 2
print(square_lambda(8))

# another lambda example
add = lambda a, b: a + b 
# a, b is arguments
# a + b is expression
print('\n' + 'Another Example: ' + '\n' + str(add(3, 5)))

# Use lambda to simple operation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
students_profile = [('Andi', 10, 'A'), ('Bryan', 15, 'A'), ('Charlie', 12, 'C'), ('Dany', 21, 'B')]

# Use lambda to map the list
squares = list(map(lambda x: x * x, numbers))
print('\n' + 'Using lambda to Map: ' + '\n' + str(squares))

# Use lambda to filter the list
filtered_even_number = list(filter(lambda x: x %2 == 0, numbers))
filtered_odd_number = list(filter(lambda x: x %2 != 0, numbers))
print('\n' + 'Using lambda to Filter even number: ' + '\n' + str(filtered_even_number))
print('\n' + 'Using lambda to Filter odd number: ' + '\n' + str(filtered_odd_number))

# use lambda to sort the list
sorted_students_age = sorted(students_profile, key=lambda x: x[1]) # x[1] means using the second parameters on the list, because parameters start with 0
sorted_students_name = sorted(students_profile, key=lambda x: x[0]) # x[0] means using the first parameters on the list, because parameters start with 0
print('\n' + 'Using lambda to sort student based on age: ' + '\n' + str(sorted_students_age))
print('\n' + 'Using lambda to sort student based on name: ' + '\n' + str(sorted_students_name))