from __future__ import annotations
from typing import List


class TreeNode(object):

    def __init__(self, x):
        self.__name = x
        self.__children: List[TreeNode] = []
        self.__files: List[str] = []

    def add_child(self, child: TreeNode):
        self.__children.append(child)

    def add_file(self, file: str):
        self.__files.append(file)

    @property
    def name(self):
        return self.__name

    @property
    def children(self):
        return self.__children

    @property
    def files(self):
        return sorted(self.__files)


def build_tree() -> TreeNode:
    stack = [TreeNode("ROOT")]
    while True:
        identity = input()
        if identity == "#":
            exit(0)

        if identity == "*":
            break

        if identity == "]":
            assert len(stack) > 1
            stack.pop()

        if identity.startswith("f"):
            stack[-1].add_file(identity)

        if identity.startswith("d"):
            node = TreeNode(identity)
            stack[-1].add_child(node)
            stack.append(node)

    assert len(stack) == 1
    return stack[0]


def print_tree(node: TreeNode, depth: int) -> None:
    print("|     " * depth + node.name)
    for child in node.children:
        print_tree(child, depth + 1)
    for file in node.files:
        print("|     " * depth + file)


def task(i):
    root = build_tree()

    print(f"DATA SET {i}:")
    print_tree(root, 0)
    print()


i = 1
while True:
    task(i)
    i += 1
