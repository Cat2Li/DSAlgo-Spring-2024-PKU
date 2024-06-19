from __future__ import annotations
from typing import Union, List


class TreeNode(object):

    def __init__(self, value: str, left: Union[TreeNode, str, None],
                 right: Union[TreeNode, str, None]):
        self.value = value
        self.left = left
        self.right = right


def build_tree(mid_order: str, post_order: str) -> TreeNode:
    root = TreeNode(post_order[-1], None, None)
    root_index = mid_order.index(root.value)

    # calculate the length of left and right sub-tree
    left_length = root_index
    right_length = len(mid_order) - root_index - 1
    assert right_length >= 0

    # build left sub-tree
    if left_length == 0:
        pass
    elif left_length == 1:
        root.left = mid_order[0]
    else:
        left_node = build_tree(mid_order[:left_length],
                               post_order[:left_length])
        root.left = left_node

    # build right sub-tree
    if right_length == 0:
        pass
    elif right_length == 1:
        root.right = mid_order[-1]
    else:
        right_node = build_tree(mid_order[-right_length:],
                                post_order[-right_length - 1:-1])
        root.right = right_node

    return root


def pre_order_builder(root: TreeNode, aux: List):
    aux.append(root.value)

    if isinstance(root.left, TreeNode):
        pre_order_builder(root.left, aux)
    elif isinstance(root.left, str):
        aux.append(root.left)
    else:
        assert root.left is None

    if isinstance(root.right, TreeNode):
        pre_order_builder(root.right, aux)
    elif isinstance(root.right, str):
        aux.append(root.right)
    else:
        assert root.right is None


mid_order = input()
post_order = input()

root = build_tree(mid_order, post_order)

res = []
pre_order_builder(root, res)

print("".join(res))
