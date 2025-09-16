# Get input number from user
number = input()

# Sort digits in descending order and join them
largest_number = "".join(sorted(number, reverse=True))

print(largest_number)
