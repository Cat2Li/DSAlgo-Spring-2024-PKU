from __future__ import annotations
from typing import Tuple, List
import sys

sys.setrecursionlimit(100000)


class KnightTour:

    def __init__(self, N: int, R: int, C: int):
        self.N = N
        self.R = R
        self.C = C

        self.moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1),
                      (-2, 1), (-2, -1)]

        self.board = [0] * (N * N)
        self.board[self.pos2idx(self.R, self.C)] = 1

        self.res = False

    def pos2idx(self, x: int, y: int) -> int:
        return x * self.N + y

    def idx2pos(self, idx: int) -> Tuple[int, int]:
        return idx // self.N, idx % self.N

    def is_legal_step(self, x: int, y: int) -> bool:
        return 0 <= x < self.N and 0 <= y < self.N and not self.board[
            self.pos2idx(x, y)]

    def is_finished(self) -> bool:
        return sum(self.board) == self.N * self.N

    def get_weight(self, x: int, y: int) -> int:
        res = 0
        for dx, dy in self.moves:
            curX = x + dx
            curY = y + dy
            if self.is_legal_step(curX, curY):
                res += 1
        return res

    def get_next_moves(self, x: int, y: int) -> List[Tuple[int, int]]:
        res = []
        for dx, dy in self.moves:
            curX = x + dx
            curY = y + dy
            if self.is_legal_step(curX, curY):
                res.append((curX, curY))
        res.sort(key=lambda x: self.get_weight(x[0], x[1]), reverse=False)
        return res

    def knight_tour_helper(self, x: int, y: int) -> None:
        for nx, ny in self.get_next_moves(x, y):
            # Return if the result is found in the previous step
            if self.res:
                return

            # Go to the next step otherwise
            self.board[self.pos2idx(nx, ny)] = 1
            if self.is_finished():
                self.res = True
                return
            self.knight_tour_helper(nx, ny)

            # Backtrack
            self.board[self.pos2idx(nx, ny)] = 0

    def knight_tour(self) -> None:
        self.knight_tour_helper(self.R, self.C)


N = int(input())
R, C = map(int, input().split())

kt = KnightTour(N, R, C)
kt.knight_tour()
print("success" if kt.res else "fail")
