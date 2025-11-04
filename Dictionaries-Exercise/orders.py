products = {}

while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price  # update price if changed

for name, data in products.items():
    total_price = data["price"] * data["quantity"]
    print(f"{name} -> {total_price:.2f}")
