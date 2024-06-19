from __future__ import annotations
from typing import Dict, List, Tuple
from numbers import Number
import heapq

PlaceName = str
PlaceNo = int


class Graph:

    def __init__(self, N: int):
        self.N = N
        self.edges: List[Dict[PlaceNo, Number]] = [{} for _ in range(N)]

    def add_edge(self, src: PlaceNo, dest: PlaceNo, dist: Number):
        self.edges[src][dest] = dist
        self.edges[dest][src] = dist

    def dijkstra(self, src: PlaceNo, dest: PlaceNo) -> List[PlaceNo]:
        queue: List[Tuple[Number, List[PlaceNo]]] = [(0, [src])]
        while queue:
            dist, path = heapq.heappop(queue)
            last = path[-1]
            if last == dest:
                return path
            for to, weight in self.edges[last].items():
                if to not in path:
                    heapq.heappush(queue, (dist + weight, path + [to]))
        raise ValueError("No path found")


d_place: Dict[PlaceName, PlaceNo] = {}
d_no: List[PlaceName] = []

P = int(input())
for i in range(P):
    place_name = input()
    d_place[place_name] = i
    d_no.append(place_name)
g = Graph(P)

Q = int(input())
for _ in range(Q):
    either, other, dist = input().split()
    dist = int(dist)

    either_no = d_place[either]
    other_no = d_place[other]

    g.add_edge(either_no, other_no, dist)


def output_path(path: List[PlaceNo]):
    global g, d_no
    res: List[str] = [d_no[path[0]]]
    for i in range(1, len(path)):
        res.append(f"->({g.edges[path[i-1]][path[i]]})->{d_no[path[i]]}")
    print("".join(res))


R = int(input())
for _ in range(R):
    src, dest = input().split()

    src_no = d_place[src]
    dest_no = d_place[dest]

    path = g.dijkstra(src_no, dest_no)
    output_path(path)
