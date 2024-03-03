def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

input_string = "Civic"
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")