def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

input_string = "Hello World! My name is Akhmi"
upper_count, lower_count = count_upper_lower(input_string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)