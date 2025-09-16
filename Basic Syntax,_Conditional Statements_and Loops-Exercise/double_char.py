while True:
    string = input()

    if string == "End":
        break
    if string == "SoftUni":
        continue

    result = ""
    for character in string:
        result += character * 2

    print(result)
