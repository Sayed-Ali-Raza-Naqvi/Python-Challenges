# Implement a function that takes a natural number as an argument and
# returns a list containing the prime factorization of that number.
# Present the solution in the form of a function called calculate().

def calculate(number):
    prime_factors = []
    divisor = 2
    
    while number > 1:
        while number % divisor == 0:
            prime_factors.append(divisor)
            number //= divisor
        
        divisor += 1
    
    return prime_factors
  
result = calculate(48)
print(result)
    
