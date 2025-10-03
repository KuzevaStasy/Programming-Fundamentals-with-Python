def min_number(first: int, second: int, third: int) -> int:
    return min(first, second, third)

first_number = int(input())
second_number = int(input())
third_number = int(input())

result = min_number(first_number, second_number, third_number)
print(result)