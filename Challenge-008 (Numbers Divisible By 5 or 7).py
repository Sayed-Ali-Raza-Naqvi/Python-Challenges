# All natural numbers divisible by 5 or 7 less than 20 are:
# [0, 5, 7, 10, 14, 15]. The sum of these numbers is: 51.
# In this exercise, we treat zero as a natural number.

# Find the sum of all numbers that are divisible by 5 or 7 less than 100.

# Present the solution in the form of a function called calculate().
# In response, call calculate() function and print the result to the console.

def calculate():
    sum = 0
    
    for num in range(100):
        if num % 5 == 0 or num % 7 == 0:
            sum += num
    
    return sum
         
result = calculate()
print(result)
