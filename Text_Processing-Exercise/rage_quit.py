import re

text = input()

# Find all pairs: (non-digit sequence)(number)
pairs = re.findall(r'(\D+)(\d+)', text)

rage_message = []

for letters, count in pairs:
    count = int(count)
    rage_message.append(letters.upper() * count)

final_message = "".join(rage_message)

unique_symbols = len(set(final_message.upper()))

print(f"Unique symbols used: {unique_symbols}")
print(final_message)
