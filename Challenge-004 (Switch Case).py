# Make a function that, given a string, returns the string with uppercase
# letters in lowercase and vice versa. Include punctuation and other non-cased
# characters unchanged.

def switch_case(string):
    new_string = ""
    
    for letter in string:
        if letter.isupper():
           new_string += letter.lower()
        else:
            new_string += letter.upper()

    return new_string

user = input("Enter a string with uppercase and lowercase characters: ")
result = switch_case(user)
print(result)
