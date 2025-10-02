product_order = input()
count_product = int(input())

coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00

def total_sum(product_kind, count):
    result = None
    if product_kind == "coffee":
        result = count * coffee_price
    elif product_kind == "coke":
        result = count * coke_price
    elif product_kind == "water":
        result = count * water_price
    elif product_kind == "snacks":
        result = count * snacks_price
    return result

total = total_sum(product_order, count_product)
print(f"{total:.2f}")