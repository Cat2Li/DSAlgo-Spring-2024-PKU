from __future__ import annotations
from typing import Dict, Deque, List
from collections import deque

upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = "abcdefghijklmnopqrstuvwxyz"


class Vertex:

    def __init__(self, key: int):
        self.key = key
        self.neighbours: Dict[int, int] = {}


class Graph:

    def __init__(self):
        self.num_vertices: int = 0
        self.vertices: Dict[int, Vertex] = {}

    def add_vertex(self, key: int):
        self.vertices[key] = Vertex(key)
        self.num_vertices += 1

    def add_edge(self, src: int, tgt: int, weight: int):
        self.vertices[src].neighbours[tgt] = weight
        self.vertices[tgt].neighbours[src] = weight

    def bfs_find(self, src: int, tgt: int):
        _path = {src: None}
        queue: Deque[int] = deque([src])
        while queue:
            cur = queue.popleft()
            if cur == tgt:
                break

            for neighbour in self.vertices[cur].neighbours.keys():
                if neighbour not in _path:
                    _path[neighbour] = cur
                    queue.append(neighbour)

        if tgt not in _path:
            return []

        path = []
        cur = tgt
        while cur is not None:
            path.append(cur)
            cur = _path[cur]

        return path[::-1]


def build_graph(N: int):
    # read words
    w2idx: Dict[str, int] = {}
    idx2w: Dict[int, str] = {}
    for i in range(N):
        word = input().strip()
        w2idx[word] = i
        idx2w[i] = word

    # initialize graph
    graph = Graph()
    for i in range(N):
        graph.add_vertex(i)

    # set letters
    if word[0].isupper():
        letters = upper_letters
    else:
        letters = lower_letters

    # add edges
    for word in w2idx.keys():
        for i in range(len(word)):
            for letter in letters:
                # skip if the letter is the same as the one in the word
                if letter == word[i]:
                    continue
                # try to add edges between word and new_word
                new_word = word[:i] + letter + word[i + 1:]
                if new_word in w2idx:
                    graph.add_edge(w2idx[word], w2idx[new_word], 1)

    return w2idx, idx2w, graph


def output_path(idx2w: Dict[str, int], path: List[int]):
    if path:
        print(" ".join([idx2w[idx] for idx in path]))
    else:
        print("NO")


if __name__ == "__main__":
    N = int(input())
    W, I, G = build_graph(N)
    src, tgt = input().strip().split()
    path = G.bfs_find(W[src], W[tgt])
    output_path(I, path)
