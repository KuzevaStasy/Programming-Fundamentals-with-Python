n = int(input())

parking = {}

for _ in range(n):
    command_parts = input().split()
    action = command_parts[0]
    username = command_parts[1]

    if action == "register":
        license_plate = command_parts[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif action == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for user, plate in parking.items():
    print(f"{user} => {plate}")
