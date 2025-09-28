numbers = list(map(int, input().split()))

while True:
    command_line = input()
    if command_line == "end":
        break

    parts = command_line.split()
    command = parts[0]

    if command == "exchange":
        index = int(parts[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            # Split and exchange
            numbers = numbers[index+1:] + numbers[:index+1]

    elif command in ("max", "min"):
        even_odd = parts[1]
        filtered = []
        for i in range(len(numbers)):
            if even_odd == "even" and numbers[i] % 2 == 0:
                filtered.append((numbers[i], i))
            elif even_odd == "odd" and numbers[i] % 2 != 0:
                filtered.append((numbers[i], i))

        if not filtered:
            print("No matches")
        else:
            if command == "max":
                value, idx = filtered[0]
                for val, i in filtered:
                    if val >= value:  # rightmost max
                        value = val
                        idx = i
            else:  # min
                value, idx = filtered[0]
                for val, i in filtered:
                    if val <= value:  # rightmost min
                        value = val
                        idx = i
            print(idx)

    elif command in ("first", "last"):
        count = int(parts[1])
        even_odd = parts[2]
        if count > len(numbers):
            print("Invalid count")
        else:
            filtered = []
            if command == "first":
                for num in numbers:
                    if even_odd == "even" and num % 2 == 0:
                        filtered.append(num)
                    elif even_odd == "odd" and num % 2 != 0:
                        filtered.append(num)
                    if len(filtered) == count:
                        break
            else:  # last
                temp = []
                for num in numbers:
                    if even_odd == "even" and num % 2 == 0:
                        temp.append(num)
                    elif even_odd == "odd" and num % 2 != 0:
                        temp.append(num)
                filtered = temp[-count:] if count <= len(temp) else temp
            print(filtered)

# Print final state of the list
print(numbers)
