# Write a function that takes a list of integers as input and returns
# a new list with only the even numbers squared.

def squared_even_numbers(numbers):
    return [number ** 2 for number in numbers if number % 2 == 0]

list_of_numbers = []

user_1 = int(input("How many numbers you want to add: "))

for i in range(user_1):
    user_2 = int(input(f"Enter number {i + 1}: "))
    list_of_numbers.append(user_2)

result = squared_even_numbers(list_of_numbers)
print(f"The even numbers after squaring are: {result}.")
    
