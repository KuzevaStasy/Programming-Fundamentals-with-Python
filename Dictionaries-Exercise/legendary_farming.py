from collections import OrderedDict

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = OrderedDict()

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

obtained = None

while not obtained:
    parts = input().lower().split()
    for i in range(0, len(parts), 2):
        qty = int(parts[i])
        material = parts[i + 1]

        if material in key_materials:
            key_materials[material] += qty
            if key_materials[material] >= 250:
                obtained = legendary_items[material]
                key_materials[material] -= 250
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += qty
    # if obtained, outer loop will exit because condition checked at top

print(f"{obtained} obtained!")

# Print key materials in the required fixed order
print(f"shards: {key_materials['shards']}")
print(f"fragments: {key_materials['fragments']}")
print(f"motes: {key_materials['motes']}")

# Print junk in order of appearance
for mat, q in junk.items():
    print(f"{mat}: {q}")
