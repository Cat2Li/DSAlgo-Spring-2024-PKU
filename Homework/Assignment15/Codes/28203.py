from typing import List
from collections import deque

N = int(input())
arr = [*map(int, input().split())]
mono_stack: List[int] = []
res = deque()

for rev_idx in range(N):
    idx = N - rev_idx - 1
    while mono_stack and arr[mono_stack[-1]] <= arr[idx]:
        mono_stack.pop()
    res.appendleft(mono_stack[-1] + 1 if mono_stack else 0)
    mono_stack.append(idx)

print(*res)
