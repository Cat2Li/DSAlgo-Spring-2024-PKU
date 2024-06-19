from __future__ import annotations
from typing import Union, Deque, List
from collections import deque
from sys import stdin
import heapq


class TreeNode(object):

    def __init__(self, val: List[str], weight: int):
        self.val = val
        self.val_set = None
        self.weight = weight
        self.left: Union[None, TreeNode] = None
        self.right: Union[None, TreeNode] = None

    def __eq__(self, other: TreeNode) -> bool:
        if self.weight == other.weight:
            return self.val == other.val
        else:
            return False

    def __gt__(self, other: TreeNode) -> bool:
        if self.weight == other.weight:
            return self.val > other.val
        else:
            return self.weight > other.weight

    def finish(self):
        self.val_set = set(self.val)


def build_tree(n) -> TreeNode:
    node_list: List[TreeNode] = []
    node_heap: List[TreeNode] = []
    for _ in range(n):
        val, weight = input().split()
        node = TreeNode([val], int(weight))
        node_list.append(node)
        heapq.heappush(node_heap, node)

    while len(node_heap) > 1:
        left = heapq.heappop(node_heap)
        right = heapq.heappop(node_heap)

        node = TreeNode(list(heapq.merge(left.val, right.val)),
                        left.weight + right.weight)
        node_list.append(node)

        node.left = left
        node.right = right

        heapq.heappush(node_heap, node)

    for node in node_list:
        node.finish()

    return node_heap[0]


def encode(root: TreeNode, string: str) -> str:
    res = []

    for char in string:
        node = root
        while True:
            if len(node.val) == 1:
                break

            if char in node.left.val_set:
                node = node.left
                res.append('0')
            else:
                node = node.right
                res.append('1')

    return ''.join(res)


def decode(root: TreeNode, string: str) -> str:
    res = []

    i = 0
    while i < len(string):
        node = root
        while True:
            # if node is leaf
            if len(node.val) == 1:
                break

            # if node is not leaf
            if string[i] == '0':
                node = node.left
            else:
                node = node.right
            i += 1
        res.append(node.val[0])

    return ''.join(res)


n = int(input())
root = build_tree(n)
for line in stdin.readlines():
    line = line.strip()
    if line[0] in root.val_set:
        print(encode(root, line))
    else:
        print(decode(root, line))
