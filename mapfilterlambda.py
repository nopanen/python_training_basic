list_of_numbers = [3, 4, 10, 15]

def square(x):
    return x * x

print(list(map(square, list_of_numbers)))
print(list(map(lambda x: x*x, list_of_numbers)))

# With list comprehension:
result = [x*x for x in list_of_numbers]
print(result)

list_of_numbers = [19, 34, 4, 2]

print(filter(lambda x: x > 10, list_of_numbers))

list_of_strings = ['John', 'Mary', 'Kevin', 'George']
print(list(filter(lambda name: name[0] == 'M' or name[0] == 'K', list_of_strings)))

def call_two(function_one, function_two, x, y):
    result_from_function_one = function_one(x, y)
    result_from_function_two = function_two(x, y)
    return result_from_function_one, result_from_function_two

print(call_two(lambda x, y: x+y, lambda x,y: x*y, 10 , 15))

list_of_different_things = [0, 1, None, '', 5]

print(list(filter(None, list_of_different_things)))