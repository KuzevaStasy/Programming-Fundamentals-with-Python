data = input().split()

while True:
    command = input()
    if command == "3:1":
        break

    parts = command.split()
    action = parts[0]

    if action == "merge":
        start = int(parts[1])
        end = int(parts[2])

        # Clamp the indices to be inside the array
        start = max(0, start)
        end = min(len(data) - 1, end)

        # Merge the elements
        merged = ''.join(data[start:end + 1])
        data = data[:start] + [merged] + data[end + 1:]

    elif action == "divide":
        index = int(parts[1])
        partitions = int(parts[2])

        element = data[index]
        part_length = len(element) // partitions
        remainder = len(element) % partitions

        new_parts = []
        start_idx = 0

        for i in range(partitions):
            add_len = part_length + (1 if i < remainder else 0)
            new_parts.append(element[start_idx:start_idx + add_len])
            start_idx += add_len

        data = data[:index] + new_parts + data[index + 1:]

print(' '.join(data))