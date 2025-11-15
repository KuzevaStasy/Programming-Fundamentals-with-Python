import re

text = input()
word = input()

# Build a regex that matches the word as a whole word, case-insensitive
pattern = rf"\b{re.escape(word)}\b"

matches = re.findall(pattern, text, flags=re.IGNORECASE)

print(len(matches))
