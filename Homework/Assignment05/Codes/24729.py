from __future__ import annotations
from typing import List, Union


class TreeNode(object):

    def __init__(self, value):
        self.value: str = value
        self.nodes: List[TreeNode] = []

    def __str__(self):
        return self.value

    def insert_node(self, node: TreeNode):
        self.nodes.append(node)


def parse_input(str_tree: str) -> TreeNode:
    root = TreeNode(str_tree[0])

    stack = [root]
    for i in range(1, len(str_tree)):
        if str_tree[i] == '(':
            continue

        if str_tree[i] == ')' or str_tree[i] == ',':
            stack.pop()
            continue

        new_node = TreeNode(str_tree[i])
        stack[-1].insert_node(new_node)
        stack.append(new_node)

    return stack[0]


def preorder_traversal(root: TreeNode, res: List[str]) -> None:
    res.append(root.value)
    for node in root.nodes:
        preorder_traversal(node, res)
    return "".join(res)


def postorder_traversal(root: TreeNode, res: List[str]) -> None:
    for node in root.nodes:
        postorder_traversal(node, res)
    res.append(root.value)
    return "".join(res)


tree_str = input()
root = parse_input(tree_str)

preorder = preorder_traversal(root, [])
postorder = postorder_traversal(root, [])
print(preorder)
print(postorder)
