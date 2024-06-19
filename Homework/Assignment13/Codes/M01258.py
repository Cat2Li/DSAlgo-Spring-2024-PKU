from __future__ import annotations
import heapq


class UnionFind:

    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(N)]
        self.size = [1] * N

    def find(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]


class UDGraph:

    def __init__(self, N):
        self.N = N
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    @staticmethod
    def kruskal(g: UDGraph):
        uf = UnionFind(g.N)
        mst = []

        queue = g.edges.copy()
        heapq.heapify(queue)

        while len(mst) < g.N - 1 and queue:
            w, u, v = heapq.heappop(queue)
            if not uf.connected(u, v):
                uf.union(u, v)
                mst.append((u, v, w))
        return mst


while True:
    try:
        N = int(input())
        arr = [[*map(int, input().split())] for _ in range(N)]

        g = UDGraph(N)
        for i in range(N):
            for j in range(i + 1, N):
                g.add_edge(i, j, arr[i][j])

        mst = UDGraph.kruskal(g)
        print(sum(w for _, _, w in mst))
    except:
        exit()
