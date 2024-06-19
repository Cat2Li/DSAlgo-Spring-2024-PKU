import heapq
from typing import List, Tuple, Dict

M, N, P = map(int, input().split())


def build_grid(M: int, N: int) -> List[List[str]]:
    grid = []
    for _ in range(M):
        grid.append(input().split())
    return grid


def is_valid(x: int, y: int):
    return 0 <= x < M and 0 <= y < N and grid[x][y] != '#'


def cost(x: int, y: int, nx: int, ny: int):
    return abs(int(grid[nx][ny]) - int(grid[x][y]))


def task(sx, sy, tx, ty):
    if not is_valid(sx, sy) or not is_valid(tx, ty):
        print('NO')
        return

    pq = []
    visited = [[False] * N for _ in range(M)]

    heapq.heappush(pq, (0, sx, sy))
    while pq:
        step, x, y = heapq.heappop(pq)

        if visited[x][y]:
            continue

        visited[x][y] = True

        if (x, y) == (tx, ty):
            print(step)
            return

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                heapq.heappush(pq, (step + cost(x, y, nx, ny), nx, ny))

    print('NO')


grid = build_grid(M, N)
for _ in range(P):
    sx, sy, tx, ty = map(int, input().split())
    task(sx, sy, tx, ty)
