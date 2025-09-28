numbers = list(map(int, input().split(", ")))

result = []

# Append non-zero numbers first
for num in numbers:
    if num != 0:
        result.append(num)

# Append zeros at the end
for num in numbers:
    if num == 0:
        result.append(num)

print(result)