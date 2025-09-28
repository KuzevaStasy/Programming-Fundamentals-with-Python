events = input().split("|")

energy = 100
coins = 100

for event in events:
    name, value = event.split("-")
    value = int(value)

    if name == "rest":
        gained = min(100 - energy, value)
        energy += gained
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")

    elif name == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:  # Buying ingredient
        if coins >= value:
            coins -= value
            print(f"You bought {name}.")
        else:
            print(f"Closed! Cannot afford {name}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
