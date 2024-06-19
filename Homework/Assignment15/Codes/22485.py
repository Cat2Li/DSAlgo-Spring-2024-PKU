from __future__ import annotations
from typing import Union, List


class TreeNode:

    def __init__(self, value: int):
        self.value = value
        self.left: Union[TreeNode, None] = None
        self.right: Union[TreeNode, None] = None


def build_tree(N) -> TreeNode:
    nodes: List[TreeNode] = [TreeNode(i + 1) for i in range(N)]
    for idx in range(N):
        a, b = map(int, input().split())
        idx_a, idx_b = a - 1, b - 1
        if idx_a != -2:
            nodes[idx].left = nodes[idx_a]
        if idx_b != -2:
            nodes[idx].right = nodes[idx_b]
    return nodes[0]


def layer_bfs(root: TreeNode) -> None:
    cur_layer = [root]
    res = []
    while cur_layer:
        res.append(cur_layer[-1].value)
        next_layer = []
        for node in cur_layer:
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        cur_layer = next_layer
    print(' '.join(map(str, res)))


N = int(input())
root = build_tree(N)
layer_bfs(root)
