import re

numbers = []

while True:
    line = input()
    if line == "":
        break
    found = re.findall(r"\d+", line)
    numbers.extend(found)

print(" ".join(numbers))
