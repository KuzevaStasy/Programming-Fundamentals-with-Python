def find_longest_path(maze, start_row, start_col):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    longest = 0

    def dfs(r, c, moves):
        nonlocal longest
        # Check if out of bounds → exit found
        if r < 0 or r >= rows or c < 0 or c >= cols:
            longest = max(longest, moves)
            return
        # Check walls or visited
        if maze[r][c] == '#' or visited[r][c]:
            return
        visited[r][c] = True
        # Explore all four directions
        dfs(r+1, c, moves+1)
        dfs(r-1, c, moves+1)
        dfs(r, c+1, moves+1)
        dfs(r, c-1, moves+1)
        visited[r][c] = False  # backtrack

    dfs(start_row, start_col, 0)
    return longest

# Read input
n = int(input())
maze = [list(input()) for _ in range(n)]
start_row = start_col = None

# Find Kate's starting position
for i in range(n):
    for j in range(len(maze[i])):
        if maze[i][j] == 'k':
            start_row, start_col = i, j
            break
    if start_row is not None:
        break

# Find the longest path to exit
longest_moves = find_longest_path(maze, start_row, start_col)

if longest_moves > 0:
    print(f"Kate got out in {longest_moves} moves")
else:
    print("Kate cannot get out")