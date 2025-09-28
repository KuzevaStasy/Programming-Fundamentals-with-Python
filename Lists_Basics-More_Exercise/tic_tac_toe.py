field = []
for _ in range(3):
    row = list(map(int, input().split()))
    field.append(row)

winner = 0  # 0 means no winner yet

# Check rows
for i in range(3):
    if field[i][0] == field[i][1] == field[i][2] != 0:
        winner = field[i][0]

# Check columns
for i in range(3):
    if field[0][i] == field[1][i] == field[2][i] != 0:
        winner = field[0][i]

# Check main diagonal
if field[0][0] == field[1][1] == field[2][2] != 0:
    winner = field[0][0]

# Check secondary diagonal
if field[0][2] == field[1][1] == field[2][0] != 0:
    winner = field[0][2]

# Print result
if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
