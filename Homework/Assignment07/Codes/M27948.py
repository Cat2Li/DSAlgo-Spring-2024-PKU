from __future__ import annotations
from typing import Union, List

N = int(input())
s = input()


class TreeNode(object):

    def __init__(self, val: str, left: Union[TreeNode, None],
                 right: Union[TreeNode, None]):
        self.val = val
        self.left = left
        self.right = right


def classify(s: str, lo: int, hi: int) -> str:
    if "0" in s[lo:hi]:
        if "1" in s[lo:hi]:
            return "F"
        else:
            return "B"
    return "I"


def build_tree(s: str, lo: int, hi: int) -> TreeNode:
    if hi - lo == 1:
        return TreeNode(classify(s, lo, hi), None, None)

    mid = (lo + hi) // 2
    left = build_tree(s, lo, mid)
    right = build_tree(s, mid, hi)
    return TreeNode(classify(s, lo, hi), left, right)


def post_order(node: TreeNode, res: List[str]):
    if node is None:
        return
    post_order(node.left, res)
    post_order(node.right, res)
    res.append(node.val)


res = []
post_order(build_tree(s, 0, len(s)), res)

print("".join(res))
