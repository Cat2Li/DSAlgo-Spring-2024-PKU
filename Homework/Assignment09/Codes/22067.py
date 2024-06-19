from sys import stdin
from typing import List


class Result():

    def __init__(self):
        self.dstack: List[int] = []

    def push(self, value: int):
        self.dstack.append(
            min(value, self.dstack[-1] if self.dstack else value))

    def pop(self):
        if self.dstack:
            self.dstack.pop()

    def min(self):
        if self.dstack:
            print(self.dstack[-1])


res = Result()
for line in stdin.readlines():
    line = line.strip()
    if line == "pop":
        res.pop()
    elif line == "min":
        res.min()
    else:
        _, value = line.split()
        res.push(int(value))
