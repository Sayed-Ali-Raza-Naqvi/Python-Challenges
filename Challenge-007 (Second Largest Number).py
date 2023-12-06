# Write a Python function to find the second largest number in a
# list of integers.

def second_largest_number(numbers):
    if len(numbers) < 2:
        return "List should contain atleast two numbers."

    largest = second = float("-inf")

    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second and number != largest:
            second = number

    return second

user_input = [10, 5, 8, 9, 4]
result = second_largest_number(user_input)
print(result)
