phonebook = {}

# Read name-number pairs until a number (N) is entered
while True:
    entry = input()
    if entry.isdigit():
        n = int(entry)
        break
    name, number = entry.split("-")
    phonebook[name] = number  # Add or update the entry

# Perform N searches
for _ in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
