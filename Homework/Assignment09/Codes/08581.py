from __future__ import annotations
from typing import Union, List, Tuple


class TreeNode:

    def __init__(self, x: str):
        self.val = x
        self.left: Union[None, TreeNode] = None
        self.right: Union[None, TreeNode] = None


def build_tree(s: str) -> TreeNode:
    stack: List[Tuple[TreeNode, int]] = []

    root = TreeNode(s[0])
    stack.append((root, 0))

    for char in s[1::]:
        if char == ".":
            cur_node, times = stack.pop()
            if times == 0:
                stack.append((cur_node, times + 1))
            else:
                while stack and times == 1:
                    parent, times = stack.pop()
                    if times == 0:
                        parent.left = cur_node
                        stack.append((parent, 1))
                    else:
                        parent.right = cur_node
                        cur_node = parent
            continue

        node = TreeNode(char)
        stack.append((node, 0))

    return root


def mid_order_traversal(root: Union[None, TreeNode], res: List[str]) -> None:
    if root is None:
        return

    mid_order_traversal(root.left, res)
    res.append(root.val)
    mid_order_traversal(root.right, res)


def post_order_traversal(root: Union[None, TreeNode], res: List[str]) -> None:
    if root is None:
        return

    post_order_traversal(root.left, res)
    post_order_traversal(root.right, res)
    res.append(root.val)


s = input()
root = build_tree(s)

mid_order = []
mid_order_traversal(root, mid_order)
print("".join(mid_order))

post_order = []
post_order_traversal(root, post_order)
print("".join(post_order))
