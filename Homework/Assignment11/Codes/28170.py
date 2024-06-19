grid = [input() for _ in range(10)]
visited = [[False] * 10 for _ in range(10)]


def dfs(x, y):
    global grid, visited
    visited[x][y] = True
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10 and grid[nx][
                ny] == "." and not visited[nx][ny]:
            dfs(nx, ny)


count = 0
for x in range(10):
    for y in range(10):
        if grid[x][y] == "." and not visited[x][y]:
            dfs(x, y)
            count += 1

print(count)
