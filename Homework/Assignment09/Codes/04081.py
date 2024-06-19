from __future__ import annotations
from typing import List, Tuple, Union, Deque
from collections import deque


class MTreeNode:

    def __init__(self, x: str):
        self.val = x
        self.children: List[MTreeNode] = []


class BTreeNode:

    def __init__(self, x: str):
        self.val = x
        self.left: Union[None, BTreeNode] = None
        self.right: Union[None, BTreeNode] = None


def build_unnamed_mtree(s: str) -> MTreeNode:
    root = MTreeNode(0)
    stack: List[MTreeNode] = [root]
    for char in s:
        if char == "d":
            node = MTreeNode(0)
            stack[-1].children.append(node)
            stack.append(node)
        elif char == "u":
            stack.pop()
    return root


def name_mtree(root: MTreeNode) -> None:
    idx = 0
    queue: Deque[MTreeNode] = deque([root])
    while queue:
        node = queue.popleft()
        node.val = idx
        idx += 1
        queue.extend(node.children)


def build_mtree(s: str) -> MTreeNode:
    root = build_unnamed_mtree(s)
    name_mtree(root)
    return root


def depth1p_mtree(root: MTreeNode) -> int:
    if not root.children:
        return 1
    return 1 + max(depth1p_mtree(child) for child in root.children)


def mtree2btree(mroot: MTreeNode) -> BTreeNode:

    def mtree2btree_helper(mnodes: List[MTreeNode]):
        if not mnodes:
            return None

        broot = BTreeNode(mnodes[0].val)
        broot.left = mtree2btree_helper(mnodes[0].children)

        bnode = broot
        for mnode in mnodes[1::]:
            bnode_ = BTreeNode(mnode.val)
            bnode.right = bnode_
            bnode = bnode_
            bnode.left = mtree2btree_helper(mnode.children)
        return broot

    broot = BTreeNode(mroot.val)
    broot.left = mtree2btree_helper(mroot.children)
    return broot


def depth1p_btree(root: Union[None, BTreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(depth1p_btree(root.left), depth1p_btree(root.right))


s = input()
mroot = build_mtree(s)
mroot_depth = depth1p_mtree(mroot) - 1
broot = mtree2btree(mroot)
broot_depth = depth1p_btree(broot) - 1
print(f"{mroot_depth} => {broot_depth}")
