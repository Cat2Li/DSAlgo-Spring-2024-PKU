from __future__ import annotations
from typing import List, Dict
from numbers import Number
import heapq


class Edge:

    def __init__(self, src: int, tgt: int, weight: Number):
        self.src = src
        self.tgt = tgt
        self.weight = weight

    def __lt__(self, other: Edge):
        return self.weight < other.weight

    def __str__(self):
        return f'Edge({self.src}, {self.tgt}, {self.weight})'


class Graph:

    def __init__(self, N):
        self.__N = N
        self.__edges: List[Edge] = []

    def add_edge(self, src: int, tgt: int, weight: Number):
        self.__edges.append(Edge(src, tgt, weight))

    @property
    def edges(self) -> List[Edge]:
        return self.__edges.copy()

    @property
    def num_vertices(self) -> int:
        return self.__N

    @property
    def num_edges(self) -> int:
        return len(self.__edges)

    def sum_weights(self) -> Number:
        return sum(edge.weight for edge in self.__edges)


class UnionFind:

    def __init__(self, N: int):
        self.N = N
        self.parent: List[int] = [i for i in range(N)]
        self.size: List[int] = [1] * N

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def build_graph():
    N = int(input())
    graph = Graph(N)

    for _ in range(N - 1):
        arr = input().split()

        src = ord(arr[0]) - 65
        num_inputs = int(arr[1])
        for j in range(2, num_inputs * 2 + 2, 2):
            tgt = ord(arr[j]) - 65
            weight = int(arr[j + 1])

            graph.add_edge(src, tgt, weight)

    return graph


def kruskal(graph: Graph):
    uf = UnionFind(graph.num_vertices)
    pq: List[Edge] = graph.edges
    mst: Graph = Graph(graph.num_vertices)
    heapq.heapify(pq)

    while pq and mst.num_edges < graph.num_vertices - 1:
        edge = heapq.heappop(pq)
        if not uf.connected(edge.src, edge.tgt):
            uf.union(edge.src, edge.tgt)
            mst.add_edge(edge.src, edge.tgt, edge.weight)

    return mst


graph = build_graph()
mst = kruskal(graph)
print(mst.sum_weights())
