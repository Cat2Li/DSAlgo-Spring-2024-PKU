from typing import List, Set, Union


class UDGraph(object):

    def __init__(self, N: int, weight: List[int]):
        assert N == len(weight)
        self.N = N
        self.weight = weight
        self.connected: List[Set[int]] = [set() for i in range(N)]
        self.visited: Union[None, List[bool]] = None

    def add_edge(self, a: int, b: int):
        self.connected[a].add(b)
        self.connected[b].add(a)

    def new_visited(self):
        self.visited = [False] * self.N

    def del_visited(self):
        self.visited = None


N, M = map(int, input().split())
arr = [*map(int, input().split())]

graph = UDGraph(N, arr)
for i in range(M):
    a, b = map(int, input().split())
    graph.add_edge(a, b)

graph.new_visited()
res = []
for i in range(N):
    stack: List[int] = []
    stack.append(i)
    value = 0
    while stack:
        v = stack.pop()
        if graph.visited[v]:
            continue
        value += graph.weight[v]
        graph.visited[v] = True
        for u in graph.connected[v]:
            if not graph.visited[u]:
                stack.append(u)
    res.append(value)

graph.del_visited()
print(max(res))
