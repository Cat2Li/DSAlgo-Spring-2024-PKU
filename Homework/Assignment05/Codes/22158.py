from __future__ import annotations
from typing import Union, List
from sys import stdin


class TreeNode(object):

    def __init__(self, value: str, left: Union[TreeNode, str, None],
                 right: Union[TreeNode, str, None]):
        self.value = value
        self.left = left
        self.right = right

    def set_left(self, left: Union[TreeNode, str]):
        self.left = left

    def set_right(self, right: Union[TreeNode, str]):
        self.right = right


def build_tree(pre_order: str, mid_order: str) -> TreeNode:
    root = TreeNode(pre_order[0], None, None)
    root_index = mid_order.index(root.value)

    # calculate the length of left and right sub-tree
    left_length = root_index
    right_length = len(pre_order) - root_index - 1
    assert right_length >= 0

    # build left sub-tree
    if left_length == 0:
        pass
    elif left_length == 1:
        root.set_left(mid_order[0])
    else:
        left_node = build_tree(pre_order[1:left_length + 1],
                               mid_order[:left_length])
        root.set_left(left_node)

    # build right sub-tree
    if right_length == 0:
        pass
    elif right_length == 1:
        root.set_right(mid_order[-1])
    else:
        right_node = build_tree(pre_order[-right_length:],
                                mid_order[-right_length:])
        root.set_right(right_node)

    return root


def post_order_builder(root: TreeNode, aux: List):
    if isinstance(root.left, TreeNode):
        post_order_builder(root.left, aux)
    elif isinstance(root.left, str):
        aux.append(root.left)
    else:
        assert root.left is None

    if isinstance(root.right, TreeNode):
        post_order_builder(root.right, aux)
    elif isinstance(root.right, str):
        aux.append(root.right)
    else:
        assert root.right is None

    aux.append(root.value)


def task(pre_order: str, mid_order: str):
    root = build_tree(pre_order, mid_order)

    res: List[str] = []
    post_order_builder(root, res)

    print("".join(res))


lines = stdin.readlines()
assert len(lines) % 2 == 0
for i in range(0, len(lines), 2):
    pre_order = lines[i].strip()
    mid_order = lines[i + 1].strip()
    task(pre_order, mid_order)
