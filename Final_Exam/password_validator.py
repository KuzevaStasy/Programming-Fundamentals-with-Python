password = input()

while True:
    command = input()
    if command == "Complete":
        break

    parts = command.split()

    if parts[0] == "Make":
        action = parts[1]
        index = int(parts[2])

        if 0 <= index < len(password):
            if action == "Upper":
                password = password[:index] + password[index].upper() + password[index+1:]
            elif action == "Lower":
                password = password[:index] + password[index].lower() + password[index+1:]
            print(password)

    elif parts[0] == "Insert":
        index = int(parts[1])
        char = parts[2]

        if 0 <= index <= len(password):
            password = password[:index] + char + password[index:]
            print(password)

    elif parts[0] == "Replace":
        char = parts[1]
        value = int(parts[2])

        if char in password:
            new_char = chr(ord(char) + value)
            password = password.replace(char, new_char)
            print(password)

    elif parts[0] == "Validation":
        # 1) Length
        if len(password) < 8:
            print("Password must be at least 8 characters long!")

        # 2) Characters allowed
        if not all(ch.isalnum() or ch == "_" for ch in password):
            print("Password must consist only of letters, digits and _!")

        # 3) At least one uppercase
        if not any(ch.isupper() for ch in password):
            print("Password must consist at least one uppercase letter!")

        # 4) At least one lowercase
        if not any(ch.islower() for ch in password):
            print("Password must consist at least one lowercase letter!")

        # 5) At least one digit
        if not any(ch.isdigit() for ch in password):
            print("Password must consist at least one digit!")
