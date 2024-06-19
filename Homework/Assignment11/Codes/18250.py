from typing import List


class UnionFind:

    def __init__(self, N: int):
        self.N = N
        self.parent = list(range(N))

    def find(self, a: int) -> int:
        while a != self.parent[a]:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)
        self.parent[b] = a

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def unique(self) -> List[int]:
        return sorted(set(self.find(i) for i in range(self.N)))


while True:
    try:
        N, M = map(int, input().split())
        uf = UnionFind(N)

        for _ in range(M):
            x, y = map(int, input().split())
            if uf.connected(x - 1, y - 1):
                print("Yes")
            else:
                uf.union(x - 1, y - 1)
                print("No")

        unique = uf.unique()
        print(len(unique))
        print(*[i + 1 for i in unique])
    except EOFError:
        break
