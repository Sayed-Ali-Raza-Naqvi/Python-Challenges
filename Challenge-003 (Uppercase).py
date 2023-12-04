# Make a function uppercase that, given a string, returns the string, with all
# letters made uppercase.


def uppercase(string):
    '''This function takes a string as an argument and returns the string with all letters in uppercase.'''

    return string.upper()

user_input = input("Enter a string to make it uppercase: ")
result = uppercase(user_input)
print(f"The uppercase of {user_input} is {result}.")
