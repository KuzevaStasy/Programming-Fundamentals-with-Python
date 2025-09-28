items = input().split("|")
budget = float(input())

max_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50,
}

bought_items = []
profit = 0

for item in items:
    type_item, price = item.split("->")
    price = float(price)

    # Check if price is valid
    if price <= max_prices[type_item]:
        if budget >= price:  # Can afford
            budget -= price
            new_price = price * 1.40
            bought_items.append(new_price)
            profit += new_price - price

# After selling items
budget += sum(bought_items)

# Output
print(" ".join([f"{p:.2f}" for p in bought_items]))
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
