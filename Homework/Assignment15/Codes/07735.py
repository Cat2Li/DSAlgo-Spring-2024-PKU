from __future__ import annotations
from typing import List, Tuple, Dict
import heapq

K = int(input())
N = int(input())
R = int(input())

T_COST = int
T_COIN = int


class Graph:

    def __init__(self, V: int):
        self.V = V
        self.edges: List[Dict[int, List[Tuple[T_COST, T_COIN]]]] = []
        self.edges = [{} for _ in range(V)]

    def add_edge(self, u: int, v: int, cost: T_COST, coin: T_COIN) -> None:
        if v in self.edges[u]:
            self.edges[u][v].append((cost, coin))
        else:
            self.edges[u][v] = [(cost, coin)]

    @staticmethod
    def dijkstra_constrained(g: Graph):
        pq: List[Tuple[T_COST, T_COIN, int]] = []
        visited: Dict[Tuple[int, T_COIN], T_COST] = {}

        heapq.heappush(pq, (0, K, 0))
        while pq:
            cost, coin, pos = heapq.heappop(pq)
            if (pos, coin) in visited and visited[(pos, coin)] <= cost:
                continue
            visited[(pos, coin)] = cost

            cur_coin = coin
            while cur_coin > 0:
                visited[(pos,
                         cur_coin)] = min(visited.get((pos, cur_coin), 10000),
                                          cost)
                cur_coin -= 1

            if pos == N - 1:
                return cost

            for nxt_pos, nxt_list in g.edges[pos].items():
                for (nxt_cost, nxt_coin) in nxt_list:
                    if coin - nxt_coin >= 0:
                        nxt_state = (cost + nxt_cost, coin - nxt_coin, nxt_pos)
                        heapq.heappush(pq, nxt_state)

        return -1


g = Graph(N)
for _ in range(R):
    S, D, L, T = map(int, input().split())
    g.add_edge(S - 1, D - 1, L, T)

print(Graph.dijkstra_constrained(g))
