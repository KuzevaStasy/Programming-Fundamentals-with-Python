first_sequence = input().split(", ")
second_sequence = input().split(", ")

result = [word for word in first_sequence if any(word in text for text in second_sequence)]

print(result)