# Find the sum of all even elements of the
# Fibonacci sequence with values less than 1,000,000 (1 million).

def calculate(number):
    previous, current = 0, 1
    sum_of_even_fibonacci_numbers = 0
    
    while current < number:
        if current % 2 == 0:
            sum_of_even_fibonacci_numbers += current
            
        previous, current = current, previous + current

    return sum_of_even_fibonacci_numbers
    
result = calculate(1000000)
print(result)
    
