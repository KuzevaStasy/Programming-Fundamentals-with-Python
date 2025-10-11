numbers = list(map(int, input().split(", ")))

group = 10
while numbers:
    current_group = [num for num in numbers if num <= group]
    print(f"Group of {group}'s: {current_group}")
    numbers = [num for num in numbers if num > group]
    group += 10
