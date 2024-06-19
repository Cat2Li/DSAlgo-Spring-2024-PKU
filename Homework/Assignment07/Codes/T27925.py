from collections import deque
from typing import Deque, Dict

group_order: Deque[int] = deque()
map_group_to_qmembers: Dict[int, Deque[int]] = dict()
map_member_to_group: Dict[int, int] = dict()

N = int(input())
for i in range(N):
    for member in map(int, input().split()):
        map_member_to_group[member] = i

for i in range(N):
    map_group_to_qmembers[i] = deque()

while True:
    command = input().split()
    if command[0] == "STOP":
        break
    elif command[0] == "ENQUEUE":
        member = int(command[1])
        group = map_member_to_group[member]
        if len(map_group_to_qmembers[group]) == 0:
            group_order.append(group)
        map_group_to_qmembers[group].append(member)
    elif command[0] == "DEQUEUE":
        group = group_order[0]
        member = map_group_to_qmembers[group].popleft()
        if len(map_group_to_qmembers[group]) == 0:
            group_order.popleft()
        print(member)
