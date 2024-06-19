from collections import deque
from typing import Tuple, List

m, n, t = map(int, input().split())
arr = [input() for _ in range(m)]


def is_valid(x: int, y: int):
    return 0 <= x < m and 0 <= y < n


def find(char: str) -> Tuple[int, int]:
    for i in range(m):
        for j in range(n):
            if arr[i][j] == char:
                return (i, j)
    raise ValueError(f"Character {char} not found")


mr_x, mr_y = find("@")
zz_x, zz_y = find("+")


def bfs():
    q = deque()
    min_step: List[List[int]] = [[10**6] * (t + 1) for _ in range(m * n)]

    # state: (lastchr, pos, left, step)
    ## pos: x * N + y
    ## left: energy left
    ## step: steps taken

    q.append((mr_x * n + mr_y, t, 0))
    while q:
        pos, left, step = q.popleft()

        if min_step[pos][left] > step:
            for energy in range(left + 1):
                min_step[pos][energy] = step
        else:
            continue

        x, y = pos // n, pos % n

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                if (nx, ny) == (zz_x, zz_y):
                    return step + 1

                npos = nx * n + ny
                nleft = left - 1 if arr[nx][ny] == "#" else left
                if nleft < 0:
                    continue

                q.append((npos, nleft, step + 1))

    return -1


print(bfs())
