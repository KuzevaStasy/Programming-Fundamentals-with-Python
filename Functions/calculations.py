input_operator = input()
first_number = int(input())
second_number = int(input())

def calculations(operator, num1, num2):
    result = None
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1 // num2   # integer division
    elif operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    return result

print(calculations(input_operator, first_number, second_number))