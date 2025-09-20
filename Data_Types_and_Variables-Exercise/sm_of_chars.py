number_of_chars = int(input())
sum_of_ascii_code = 0

for i in range(number_of_chars):
    char = input()
    sum_of_ascii_code += ord(char)

print(f"The sum equals: {sum_of_ascii_code}")
