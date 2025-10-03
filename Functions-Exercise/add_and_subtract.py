def sum_numbers(num1, num2):
    return num1 + num2

def subtract(returned, third):
    return returned - third

def add_and_subtract(first, second, third):
    result = sum_numbers(first, second)
    final_result = subtract(result, third)
    print(final_result)

first_number = int(input())
second_number = int(input())
third_number = int(input())

add_and_subtract(first_number, second_number, third_number)