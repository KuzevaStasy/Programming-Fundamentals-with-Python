# Read words from input
words = input().lower().split()

# Count occurrences
counts = {}

for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

# Print words with odd occurrences
odd_words = []
for word, count in counts.items():
    if count % 2 != 0:
        odd_words.append(word)

print(" ".join(odd_words))
