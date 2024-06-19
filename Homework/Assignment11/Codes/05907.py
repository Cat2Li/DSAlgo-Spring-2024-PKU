from __future__ import annotations
from typing import Union, List


class TreeNode:

    def __init__(self, x: int):
        self.val = x
        self.parent: Union[TreeNode, None] = None
        self.left: Union[TreeNode, None] = None
        self.right: Union[TreeNode, None] = None

    def set_parent(self, parent: TreeNode):
        assert self.parent is None
        self.parent = parent

    def update_child(self, orig: TreeNode, new: TreeNode):
        if self.left is orig:
            self.left = new
        elif self.right is orig:
            self.right = new
        else:
            raise ValueError("Orig is not child of node")
        new.parent = self


def build_tree(N: int):
    nodes = [TreeNode(i) for i in range(N)]
    for _ in range(N):
        X, Y, Z = map(int, input().split())
        if Y != -1:
            nodes[X].left = nodes[Y]
            nodes[Y].set_parent(nodes[X])
        if Z != -1:
            nodes[X].right = nodes[Z]
            nodes[Z].set_parent(nodes[X])
    return nodes


def manipulate(M: int, nodes: List[TreeNode]):
    for _ in range(M):
        ty, *arg = map(int, input().split())
        if ty == 1:
            either = nodes[arg[0]]
            other = nodes[arg[1]]
            p_either = either.parent
            p_other = other.parent
            if id(p_either) == id(p_other):
                p_either.left, p_either.right = p_either.right, p_either.left
            else:
                p_either.update_child(either, other)
                p_other.update_child(other, either)
        elif ty == 2:
            node = nodes[arg[0]]
            while node.left is not None:
                node = node.left
            print(node.val)
        else:
            raise ValueError


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        nodes = build_tree(N)
        manipulate(M, nodes)
