force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")

        # Add the side if it doesn't exist
        if force_side not in force_book:
            force_book[force_side] = []

        # Add the user only if they don't exist in any side
        if not any(force_user in users for users in force_book.values()):
            force_book[force_side].append(force_user)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")

        # Remove user from any previous side
        for users in force_book.values():
            if force_user in users:
                users.remove(force_user)
                break

        # Add side if it doesn't exist
        if force_side not in force_book:
            force_book[force_side] = []

        # Add user to the new side
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

# Print sides with their members (skip sides with 0 members)
for side, users in force_book.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
