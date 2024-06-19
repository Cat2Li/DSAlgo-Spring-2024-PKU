from __future__ import annotations
from typing import Union, List
import bisect


class TreeNode(object):

    def __init__(self, val: int):
        self.val = val
        self.left: Union[None, TreeNode] = None
        self.right: Union[None, TreeNode] = None

    def set_left(self, node: TreeNode):
        self.left = node

    def set_right(self, node: TreeNode):
        self.right = node


def build_tree(arr: List[int], lo: int, hi: int) -> TreeNode:
    assert len(arr) > 0
    root = TreeNode(arr[lo])
    next_id = bisect.bisect_left(arr, arr[lo], lo + 1, hi)

    # build left node
    if next_id != lo + 1:
        root.left = build_tree(arr, lo + 1, next_id)

    # build right node
    if next_id != hi:
        root.right = build_tree(arr, next_id, hi)

    return root


def post_order_builder(root: TreeNode, aux: List[int]):
    if isinstance(root.left, TreeNode):
        post_order_builder(root.left, aux)
    if isinstance(root.right, TreeNode):
        post_order_builder(root.right, aux)
    aux.append(root.val)


n = int(input())
arr = [*map(int, input().split())]

root = build_tree(arr, 0, len(arr))

res: List[int] = []
post_order_builder(root, res)

print(" ".join(map(str, res)))
