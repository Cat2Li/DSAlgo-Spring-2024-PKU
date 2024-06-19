from __future__ import annotations
from sys import stdin
from typing import List, Union


class TreeNode:

    def __init__(self, value: str):
        self.value = value
        self.left: Union[None, TreeNode] = None
        self.right: Union[None, TreeNode] = None


def build_tree(pre_order: str, mid_order: str) -> TreeNode:
    if not pre_order:
        return None

    root = TreeNode(pre_order[0])
    root_index = mid_order.index(pre_order[0])

    root.left = None if root_index == 0 else build_tree(
        pre_order[1:root_index + 1], mid_order[:root_index])
    root.right = None if root_index == len(mid_order) - 1 else build_tree(
        pre_order[root_index + 1:], mid_order[root_index + 1:])

    return root


def post_order_traversal_helper(root: TreeNode, post_order: List[str]) -> None:
    if root is None:
        return

    post_order_traversal_helper(root.left, post_order)
    post_order_traversal_helper(root.right, post_order)
    post_order.append(root.value)


def post_order_traversal(root: TreeNode) -> str:
    post_order = []
    post_order_traversal_helper(root, post_order)
    return ''.join(post_order)


def task(pre_order: str, mid_order: str):
    root = build_tree(pre_order, mid_order)
    post_order = post_order_traversal(root)
    print(post_order)


for line in stdin.readlines():
    pre_order, mid_order = line.strip().split()
    task(pre_order, mid_order)
