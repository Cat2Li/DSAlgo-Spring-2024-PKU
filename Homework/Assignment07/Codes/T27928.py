from __future__ import annotations
from typing import List, Dict, Union


class TreeNode(object):

    def __init__(self, val: int, children: List[int]):
        self.val = val
        self.children = children

    def __eq__(self, other: TreeNode) -> bool:
        return self.val == other.val

    def __lt__(self, other: TreeNode) -> bool:
        return self.val < other.val


N = int(input())

all_nodes: Dict[int, TreeNode] = {}
parent_dict: Dict[int, int] = {}
for i in range(N):
    val, *children = map(int, input().split())

    node = TreeNode(val, sorted(children))
    all_nodes[val] = node

    for child in children:
        parent_dict[child] = val


def post_order(node: TreeNode, res: List[int]) -> List[int]:
    aux = node.val
    for child in node.children:
        if aux is not None and child > aux:
            res.append(aux)
            aux = None
        post_order(all_nodes[child], res)
    if aux is not None:
        res.append(node.val)
    return res


def find_root_idx(parent_dict: Dict[int, int]) -> int:
    root = [*parent_dict.keys()][0]
    while root in parent_dict:
        root = parent_dict[root]
    return root


root = all_nodes[find_root_idx(parent_dict)]
print("\n".join(map(str, post_order(root, []))))
