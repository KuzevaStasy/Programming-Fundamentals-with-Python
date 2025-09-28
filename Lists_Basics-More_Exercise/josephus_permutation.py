people = list(map(int, input().split()))
k = int(input())

executed = []
index = 0  # start counting from the first person

while people:
    # Calculate index of next person to execute
    index = (index + k - 1) % len(people)
    executed.append(people.pop(index))

# Print result
print(f"[{','.join(map(str, executed))}]")
