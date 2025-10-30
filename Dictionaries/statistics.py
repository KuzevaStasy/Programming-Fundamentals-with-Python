# Create an empty dictionary for storing products and their quantities
products = {}

while True:
    command = input()

    if command == "statistics":
        break

    # Split the input line into product and quantity
    product, quantity = command.split(": ")
    quantity = int(quantity)

    # Add or update the quantity
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

# Print the results
print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
