# Read the field
n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

# Read the attacks
attacks = input().split()

destroyed_ships = 0

for attack in attacks:
    row, col = map(int, attack.split('-'))
    if 0 <= row < n and 0 <= col < len(field[row]):
        if field[row][col] > 0:
            field[row][col] -= 1
            if field[row][col] == 0:
                destroyed_ships += 1

print(destroyed_ships)
