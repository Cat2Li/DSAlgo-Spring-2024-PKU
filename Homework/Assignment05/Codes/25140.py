from __future__ import annotations
from collections import deque
from typing import Union, Deque, List

OP_SET = set(chr(65 + i) for i in range(26))
NUM_SET = set(chr(97 + i) for i in range(26))


class TreeNode(object):

    def __init__(self, value: str, left: Union[TreeNode, str],
                 right: Union[TreeNode, str]):
        self.value = value
        self.left = left
        self.right = right


def build_tree() -> TreeNode:
    s = input()
    stack = []
    for char in s:
        if char in OP_SET:
            right = stack.pop()
            left = stack.pop()
            assert right is not str or right not in OP_SET
            assert left is not str or left not in OP_SET
            stack.append(TreeNode(char, left, right))
        elif char in NUM_SET:
            stack.append(char)
        else:
            raise ValueError

    assert len(stack) == 1
    return stack[0]


def bfs(root: TreeNode) -> str:
    q: Deque[Union[TreeNode, str]] = deque([root])

    res: List[str] = []
    while q:
        id = q.popleft()
        if isinstance(id, TreeNode):
            res.append(id.value)
            q.append(id.left)
            q.append(id.right)
        elif isinstance(id, str):
            res.append(id)
        else:
            raise ValueError

    return "".join(reversed(res))


def task():
    root = build_tree()
    output = bfs(root)
    print(output)


n = int(input())
for _ in range(n):
    task()
