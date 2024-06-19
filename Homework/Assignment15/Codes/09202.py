from __future__ import annotations
from typing import List, Set


class DGraph:

    def __init__(self, V: int):
        self.V = V
        self.edges: List[Set[int]] = [set() for _ in range(V)]
        self.rev_edges: List[Set[int]] = [set() for _ in range(V)]

    def add_edge(self, u: int, v: int) -> None:
        self.edges[u].add(v)
        self.rev_edges[v].add(u)

    @staticmethod
    def topological_sort(g: DGraph) -> List[int]:
        stack: List[int] = []
        for i in range(g.V):
            if not g.rev_edges[i]:
                stack.append(i)

        order: List[int] = []
        while stack:
            node = stack.pop()
            order.append(node)
            for neighbor in g.edges[node]:
                g.rev_edges[neighbor].remove(node)
                if not g.rev_edges[neighbor]:
                    stack.append(neighbor)
            g.edges[node].clear()

        if len(order) != g.V:
            return []

        return order


def task() -> bool:
    N, M = map(int, input().split())
    g = DGraph(N)
    for _ in range(M):
        a, b = map(int, input().split())
        g.add_edge(a - 1, b - 1)

    return False if DGraph.topological_sort(g) else True


T = int(input())
for _ in range(T):
    result = task()
    print("Yes" if result else "No")
