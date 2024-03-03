def all_elements_true(tup):
    return all(tup)

my_tuple = (True, True, False, True)
result = all_elements_true(my_tuple)
print("All elements of the tuple are True:", result)