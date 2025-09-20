capacity = 255
current = 0

n = int(input())

for _ in range(n):
    liters = int(input())
    if current + liters > capacity:
        print("Insufficient capacity!")
    else:
        current += liters

print(current)
