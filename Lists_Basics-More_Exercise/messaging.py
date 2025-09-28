numbers = input().split()
text = list(input())

message = []

for number in numbers:
    # Calculate the sum of digits
    total = 0
    for digit in number:
        total += int(digit)

    # Wrap around if needed
    index = total % len(text)

    # Add character to message and remove it from text
    message.append(text[index])
    text.pop(index)

# Print the final message
print("".join(message))