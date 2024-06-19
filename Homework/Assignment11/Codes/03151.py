from collections import deque
from typing import Tuple, Deque, Set, List

A, B, C = map(int, input().split())

# A >= B
IDX = [1, 2] if A >= B else [2, 1]
if A < B:
    A, B = B, A
A_IDX = 0
B_IDX = 1

queue: Deque[Tuple[Tuple[int, int], List[str]]] = deque()
visited: Set[Tuple[int, int]] = set()

queue.append(((0, 0), []))
while queue:
    state, ops = queue.popleft()
    if state[0] == C or state[1] == C:
        print(len(ops))
        print("\n".join(ops))
        exit()

    if state in visited:
        continue
    visited.add(state)

    # FILL
    queue.append(((A, state[1]), ops + [f"FILL({IDX[A_IDX]})"]))
    queue.append(((state[0], B), ops + [f"FILL({IDX[B_IDX]})"]))

    # DROP
    queue.append(((0, state[1]), ops + [f"DROP({IDX[A_IDX]})"]))
    queue.append(((state[0], 0), ops + [f"DROP({IDX[B_IDX]})"]))

    # POUR
    ## A to B
    out = min(B - state[1], state[0])
    queue.append(((state[0] - out, state[1] + out),
                  ops + [f"POUR({IDX[A_IDX]},{IDX[B_IDX]})"]))
    ## B to A
    out = min(A - state[0], state[1])
    queue.append(((state[0] + out, state[1] - out),
                  ops + [f"POUR({IDX[B_IDX]},{IDX[A_IDX]})"]))

print("impossible")
