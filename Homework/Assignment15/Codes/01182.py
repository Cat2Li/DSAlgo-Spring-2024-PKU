class UnionFind:

    def __init__(self, N: int):
        self.parent = [i for i in range(N)]
        self.size = [1] * (N)

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parent[y] = x
        self.size[x] += self.size[y]

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


N, K = map(int, input().split())
uf = UnionFind(3 * N)
count = 0
for _ in range(K):
    D, X, Y = map(int, input().split())

    if X > N or Y > N:
        count += 1
        continue

    if D == 2 and X == Y:
        count += 1
        continue

    idx_X, idx_Y = X - 1, Y - 1
    if D == 1:
        if uf.connected(idx_X, idx_Y + N) or uf.connected(
                idx_X, idx_Y + 2 * N):
            count += 1
        else:
            uf.union(idx_X, idx_Y)
            uf.union(idx_X + N, idx_Y + N)
            uf.union(idx_X + 2 * N, idx_Y + 2 * N)
    elif D == 2:
        if uf.connected(idx_X, idx_Y) or uf.connected(idx_X, idx_Y + 2 * N):
            count += 1
        else:
            uf.union(idx_X, idx_Y + N)
            uf.union(idx_X + N, idx_Y + 2 * N)
            uf.union(idx_X + 2 * N, idx_Y)
    else:
        raise ValueError

print(count)
