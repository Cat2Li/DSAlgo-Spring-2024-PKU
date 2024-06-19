from __future__ import annotations
from typing import Union, List, Tuple


class MTreeNode:

    def __init__(self, val: str):
        self.val = val
        self.children: List[MTreeNode] = []


class BTreeNode:

    def __init__(self, val: str):
        self.val = val
        self.left: Union[BTreeNode, None] = None
        self.right: Union[BTreeNode, None] = None


def build_binary_tree() -> BTreeNode:
    _ = int(input())
    nodes = input().split()

    binary_root = BTreeNode(nodes[0][0])

    stack: List[Tuple[BTreeNode, int]] = [(binary_root, 0)]
    for node in nodes[1:]:
        cur, cnt = stack.pop()
        while cnt == 2:
            cur, cnt = stack.pop()
        stack.append((cur, cnt + 1))

        name, kind = node[0], node[1]

        if name == "$":
            assert kind == "1"
            continue

        new_node = BTreeNode(name)
        if cnt == 0:
            cur.left = new_node
        else:
            cur.right = new_node

        if kind == "0":
            stack.append((new_node, 0))

    while stack:
        node, node_cnt = stack.pop()
        assert node_cnt == 2

    return binary_root


def binary_to_multi(binary_root: BTreeNode) -> MTreeNode:

    def helper(node: Union[BTreeNode, None], parent: MTreeNode):
        if node is None:
            return

        multi_node = MTreeNode(node.val)
        parent.children.append(multi_node)
        helper(node.left, multi_node)
        helper(node.right, parent)

    multi_root = MTreeNode(binary_root.val)
    helper(binary_root.left, multi_root)
    assert binary_root.right is None

    return multi_root


def reverse(multi_node: MTreeNode):
    if multi_node is None:
        return

    multi_node.children.reverse()
    for child in multi_node.children:
        reverse(child)


def layer_order_traversal(multi_node: MTreeNode):

    def helper(multi_node: MTreeNode, res: List[str]):
        if multi_node is None:
            return

        queue = [multi_node]
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            queue.extend(node.children)

    res = []
    helper(multi_node, res)
    return " ".join(res)


binary_root = build_binary_tree()
multi_root = binary_to_multi(binary_root)
reverse(multi_root)
print(layer_order_traversal(multi_root))
