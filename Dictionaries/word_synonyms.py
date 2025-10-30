# Read number of words
n = int(input())

# Create an empty dictionary
synonyms = {}

# Read words and their synonyms
for _ in range(n):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

# Print the result
for word, synonym_list in synonyms.items():
    print(f"{word} - {', '.join(synonym_list)}")
