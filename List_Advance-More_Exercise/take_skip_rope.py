data = input()

numbers = [int(ch) for ch in data if ch.isdigit()]
non_numbers = [ch for ch in data if not ch.isdigit()]

take_list = numbers[::2]  # even indices
skip_list = numbers[1::2]  # odd indices

result = []
index = 0

for take, skip in zip(take_list, skip_list):
    result.extend(non_numbers[index:index+take])
    index += take + skip

# If take_list is longer than skip_list, take remaining characters
if len(take_list) > len(skip_list):
    result.extend(non_numbers[index:index+take_list[-1]])

print("".join(result))