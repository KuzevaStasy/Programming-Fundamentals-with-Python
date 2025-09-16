# Read input string from user
text = input().lower()

# Words to count
keywords = ["sand", "water", "fish", "sun"]

# Count each keyword
count = 0
for word in keywords:
    count += text.count(word)

print(count)
