# Implement a function that returns the number of all three-digit
# palindromic numbers.

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def calculate():
    count = 0
    
    for num in range(100, 1000):
        if is_palindrome(num):
            count += 1
    
    return count

result = calculate()
print(result)
