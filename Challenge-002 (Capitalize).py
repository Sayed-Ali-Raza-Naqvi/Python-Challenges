# Make a function uppercase that, given a string, returns the string, with just
# the first letter made uppercase.

def capitalize(string):
    '''This function takes a string as an argument and returns the string with only first letter capitalized.'''

    return string.capitalize()

user_input = input("Enter a string to capitalize: ")
result = capitalize(user_input)
print(f"The capitalized form of {user_input} is {result}.")
