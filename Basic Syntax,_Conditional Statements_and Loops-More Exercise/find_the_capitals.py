word = input()
# List of indices
indices = []
# Loop through each character with its index
for i in range(len(word)):
    if word[i].isupper():  # check if it's a capital letter
        indices.append(i)

print(indices)