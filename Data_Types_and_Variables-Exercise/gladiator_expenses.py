lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_breaks = 0

for fight in range(1, lost_fights + 1):
    helmet_broken = fight % 2 == 0
    sword_broken = fight % 3 == 0

    if helmet_broken:
        expenses += helmet_price
    if sword_broken:
        expenses += sword_price

    if helmet_broken and sword_broken:  # both break in same fight
        expenses += shield_price
        shield_breaks += 1

        if shield_breaks % 2 == 0:  # every 2nd shield break
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
