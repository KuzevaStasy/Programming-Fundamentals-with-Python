budget = float(input())
flour_price = float(input())

# Calculate ingredient prices
eggs_price = flour_price * 0.75
milk_price_per_litre = flour_price * 1.25
milk_price_per_loaf = milk_price_per_litre * 0.25

# Cost for one loaf
loaf_cost = eggs_price + flour_price + milk_price_per_loaf

loaves = 0
eggs = 0
money_left = budget

while money_left >= loaf_cost:
    loaves += 1
    money_left -= loaf_cost
    eggs += 3

    if loaves % 3 == 0:
        eggs -= (loaves - 2)

print(f"You made {loaves} loaves of Easter bread! Now you have {eggs} eggs and {money_left:.2f}BGN left.")
