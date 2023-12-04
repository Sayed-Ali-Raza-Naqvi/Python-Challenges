# Make a function lowercase that, given a string, returns the string, except
# in all lowercase letters.

def lowercase(string):
    '''This function takes a string as argument and returns a string in lowercase letters.'''

    return string.lower()

user_input = input("Enter a string to convert it into lowercase: ")
result = lowercase(user_input)
print(f"The lowercase of {user_input} is {result}.")
