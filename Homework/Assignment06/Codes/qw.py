from typing import List


class TreeNode(object):

    def __init__(self, key: int):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree(object):

    def __init__(self):
        self.root = None

    def insert(self, key: int) -> None:
        self.root = self.__insert(self.root, key)

    def __get_height(self, root: TreeNode) -> int:
        return 0 if root is None else root.height

    def __update_height(self, root: TreeNode) -> None:
        left_height = self.__get_height(root.left)
        right_height = self.__get_height(root.right)
        root.height = max(left_height, right_height) + 1

    def __get_balance_factor(self, root: TreeNode) -> int:
        left_height = self.__get_height(root.left)
        right_height = self.__get_height(root.right)
        return left_height - right_height

    def __right_rotate(self, root: TreeNode) -> TreeNode:
        left = root.left
        root.left = left.right
        left.right = root

        self.__update_height(root)
        self.__update_height(left)

        return left

    def __left_rotate(self, root: TreeNode) -> TreeNode:
        right = root.right
        root.right = right.left
        right.left = root

        self.__update_height(root)
        self.__update_height(right)

        return right

    def __insert(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self.__insert(root.left, key)
        elif key > root.key:
            root.right = self.__insert(root.right, key)
        else:
            # ignore duplicate
            return root

        self.__update_height(root)

        balance_factor = self.__get_balance_factor(root)

        if balance_factor > 1:
            if key < root.left.key:
                # left-left case
                root = self.__right_rotate(root)
            else:
                # left-right case
                root.left = self.__left_rotate(root.left)
                root = self.__right_rotate(root)
        elif balance_factor < -1:
            if key > root.right.key:
                # right-right case
                root = self.__left_rotate(root)
            else:
                # right-left case
                root.right = self.__right_rotate(root.right)
                root = self.__left_rotate(root)

        return root

    def insert(self, key: int) -> None:
        self.root = self.__insert(self.root, key)

    def __pre_order(self, root: TreeNode, res: List[int]):
        if root is None:
            return
        res.append(root.key)
        self.__pre_order(root.left, res)
        self.__pre_order(root.right, res)

    def pre_order(self):
        res: List[int] = []
        self.__pre_order(self.root, res)
        return " ".join(map(str, res))


n = int(input())
arr = [*map(int, input().split())]

avl_tree = AVLTree()
for val in arr:
    avl_tree.insert(val)

print(avl_tree.pre_order())
