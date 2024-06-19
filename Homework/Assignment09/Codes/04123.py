from typing import List, Tuple
from copy import deepcopy


class KnightCount:

    def __init__(self, N: int, M: int, X: int, Y: int):
        self.N = N
        self.M = M
        self.X = X
        self.Y = Y

        self.moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1),
                      (-2, 1), (-2, -1)]

        self.board = [0] * (M * N)
        self.board[self.pos2idx(X, Y)] = 1

        self.count_num = 0

    def pos2idx(self, x: int, y: int) -> int:
        return x * self.M + y

    def idx2pos(self, idx: int) -> Tuple[int, int]:
        return idx // self.M, idx % self.M

    def is_finished(self) -> bool:
        return sum(self.board) == self.N * self.M

    def is_legal_move(self, x: int, y: int) -> bool:
        return 0 <= x < self.N and 0 <= y < self.M and not self.board[
            self.pos2idx(x, y)]

    def count_helper(self, x: int, y: int):
        for dX, dY in self.moves:
            newX = x + dX
            newY = y + dY
            if not self.is_legal_move(newX, newY):
                continue

            self.board[self.pos2idx(newX, newY)] = 1
            if self.is_finished():
                self.count_num += 1
            self.count_helper(newX, newY)
            self.board[self.pos2idx(newX, newY)] = 0

    def count(self):
        self.count_helper(self.X, self.Y)


def task(N: int, M: int, X: int, Y: int):
    kc = KnightCount(N, M, X, Y)
    kc.count()
    print(kc.count_num)


T = int(input())
for _ in range(T):
    N, M, X, Y = map(int, input().split())
    task(N, M, X, Y)
