resources = {}

while True:
    resource = input()
    if resource.lower() == "stop":
        break
    quantity = int(input())

    if resource not in resources:
        resources[resource] = 0
    resources[resource] += quantity

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
