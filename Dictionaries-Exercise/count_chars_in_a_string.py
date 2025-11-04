text = input()

char_counts = {}

for char in text:
    if char != " ":
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1

for char, count in char_counts.items():
    print(f"{char} -> {count}")