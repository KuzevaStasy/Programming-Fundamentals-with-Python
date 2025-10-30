# Read the input list of characters
chars = input().split(", ")

# Create the dictionary using comprehension
ascii_dict = {ch: ord(ch) for ch in chars}

# Print the result
print(ascii_dict)
