def dfs(r, c):
    if r < 0 or r >= n or c < 0 or c >= len(board[r]) or board[r][c] != '.':
        return 0
    board[r][c] = '#'  # mark as visited
    count = 1
    # explore all 4 directions
    count += dfs(r + 1, c)
    count += dfs(r - 1, c)
    count += dfs(r, c + 1)
    count += dfs(r, c - 1)
    return count

# Read input
n = int(input())
board = [input().split() for _ in range(n)]

max_dots = 0

for i in range(n):
    for j in range(len(board[i])):
        if board[i][j] == '.':
            max_dots = max(max_dots, dfs(i, j))

print(max_dots)