class UnionFind(object):
    """
    UnionFind data structure for maintaining disjoint sets.
    Time complexity: N + M lg* N, where lg* is the iterated logarithm.
    """

    def __init__(self, N: int):
        self.__id = [*range(N)]
        self.__sz = [1 for _ in range(N)]

    def __find(self, p: int) -> int:
        """
        Find the set identifier for the element p.
        Time complexity: lg* N.
        """
        while p != self.__id[p]:
            # One-pass path compression
            self.__id[p] = self.__id[self.__id[p]]
            p = self.__id[p]
        return p

    def union(self, p: int, q: int) -> None:
        """
        Merge the sets containing elements p and q.
        Time complexity: lg* N.
        """
        i, j = self.__find(p), self.__find(q)
        if i == j:
            return
        if self.__sz[i] < self.__sz[j]:
            self.__id[i] = j
            self.__sz[j] += self.__sz[i]
        else:
            self.__id[j] = i
            self.__sz[i] += self.__sz[j]

    def connected(self, p: int, q: int) -> bool:
        """
        Check if the elements p and q are in the same set.
        Time complexity: lg* N.
        """
        return self.__find(p) == self.__find(q)

    def count(self) -> int:
        """
        Count the number of disjoint sets.
        Time complexity: N.
        """
        return sum(1 for i, id in enumerate(self.__id) if i == id)


def task(id):
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        exit(0)

    uf = UnionFind(n)
    for _ in range(m):
        p, q = map(int, input().split())
        uf.union(p - 1, q - 1)

    print(f"Case {id}: {uf.count()}")


id = 1
while True:
    task(id)
    id += 1
