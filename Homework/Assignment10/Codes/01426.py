from typing import List, Set, Tuple, Deque
from collections import deque


def task(n: int):
    q: Deque[int] = deque()
    q.append((1 % n, "1"))
    visited: Set[int] = set([1 % n])

    while q:
        mod, s = q.popleft()
        if mod == 0:
            print(s)
            return

        for digit in [0, 1]:
            new_mod = (mod * 10 + digit) % n
            new_s = s + str(digit)

            if new_mod not in visited:
                visited.add(new_mod)
                q.append((new_mod, new_s))


while True:
    if (n := int(input())) == 0:
        break
    task(n)
