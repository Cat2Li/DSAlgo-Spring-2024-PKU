N, M = map(int, input().split())


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


uf = UnionFind(N)
connected = False
loop = False

for i in range(M):
    u, v = map(int, input().split())
    if uf.connected(u, v):
        loop = True
    uf.union(u, v)

if len(set(uf.find(i) for i in range(N))) == 1:
    connected = True

if connected:
    print("connected:yes")
else:
    print("connected:no")

if loop:
    print("loop:yes")
else:
    print("loop:no")
