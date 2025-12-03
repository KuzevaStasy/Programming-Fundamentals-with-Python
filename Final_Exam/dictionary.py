# Read input
pairs = input().split(" | ")
test_words = input().split(" | ")
command = input()

# Store all words with multiple definitions
notebook = {}

for pair in pairs:
    word, definition = pair.split(": ")
    if word not in notebook:
        notebook[word] = []
    notebook[word].append(definition)

if command == "Test":
    for word in test_words:
        if word in notebook:
            print(f"{word}:")
            for definition in notebook[word]:
                print(f" -{definition}")

elif command == "Hand Over":
    # print only the words from the notebook
    print(" ".join(notebook.keys()))
