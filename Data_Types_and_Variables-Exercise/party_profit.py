group_size = int(input())
days = int(input())

coins = 0

for day in range(1, days + 1):

    # Every 10th day, 2 companions leave
    if day % 10 == 0:
        group_size -= 2

    # Every 15th day, 5 new companions join
    if day % 15 == 0:
        group_size += 5

    # Daily income
    coins += 50

    # Daily food expenses
    coins -= group_size * 2

    # Every 3rd day -> motivational party
    if day % 3 == 0:
        coins -= group_size * 3

    # Every 5th day -> slay boss monster
    if day % 5 == 0:
        coins += group_size * 20
        if day % 3 == 0:  # party on the same day
            coins -= group_size * 2

# Final result
coins_per_companion = coins // group_size
print(f"{group_size} companions received {coins_per_companion} coins each.")
