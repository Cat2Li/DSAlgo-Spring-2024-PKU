from __future__ import annotations
from typing import Union, List, Deque
from collections import deque


class TreeNode(object):

    def __init__(self, val: int):
        self.val = val
        self.left: Union[None, TreeNode] = None
        self.right: Union[None, TreeNode] = None

    def set_left(self, node: TreeNode):
        self.left = node

    def set_right(self, node: TreeNode):
        self.right = node


class BST(object):

    def __init__(self):
        self.root: TreeNode = None

    def __put(self, node: TreeNode, val: int) -> Union[TreeNode, None]:

        if node is None:
            return TreeNode(val)

        if val < node.val:
            node.left = self.__put(node.left, val)
            return node
        elif val > node.val:
            node.right = self.__put(node.right, val)
            return node

        # ignore duplicate
        return node

    def put(self, val: int) -> None:
        self.root = self.__put(self.root, val)

    def level_order(self) -> List[int]:
        queue: Deque[TreeNode] = deque([self.root])
        res: List[int] = []

        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return res


arr = [*map(int, input().split())]

bst = BST()
for val in arr:
    bst.put(val)

level_order = bst.level_order()
print(" ".join(map(str, level_order)))
