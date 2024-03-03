from functools import reduce
import operator

def multiply_list(numbers):
    if not numbers:
        return 0 
    return reduce(operator.mul, numbers)

numbers_list = [1, 2, 3, 4, 5]
result = multiply_list(numbers_list)
print("Result:", result)