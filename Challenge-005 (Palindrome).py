# Write a function to check if a string is palindrome.

def is_palindrome(string):
    string = string.lower()

    return string == string[::-1]

user = input("Enter a string to check if it is a palindrome: ")
result = is_palindrome(user)
print(f"The string '{user}' is a paindrome: {result}.")
