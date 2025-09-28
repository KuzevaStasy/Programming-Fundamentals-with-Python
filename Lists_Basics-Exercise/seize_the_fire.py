fires = input().split("#")
water = int(input())

# Valid ranges
ranges = {
    "High": range(81, 126),
    "Medium": range(51, 81),
    "Low": range(1, 51),
}

cells_put_out = []
effort = 0
total_fire = 0

for fire in fires:
    type_fire, value = fire.split(" = ")
    value = int(value)

    # Check if valid fire cell
    if value in ranges[type_fire]:
        if water >= value:
            water -= value
            cells_put_out.append(value)
            effort += value * 0.25
            total_fire += value
        # if not enough water, skip

# Print results
print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")