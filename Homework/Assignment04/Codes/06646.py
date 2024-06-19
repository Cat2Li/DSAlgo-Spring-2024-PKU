class TreeNode(object):

    def __init__(self):
        self.left = None
        self.right = None


def tree_depth(node, level):
    if node is None:
        return 0
    return max(tree_depth(node.left, level + 1),
               tree_depth(node.right, level + 1)) + 1


N = int(input())
Trees = [TreeNode() for _ in range(N)]
for i in range(N):
    l, r = map(int, input().split())
    if l > 0:
        Trees[i].left = Trees[l - 1]
    if r > 0:
        Trees[i].right = Trees[r - 1]
print(tree_depth(Trees[0], 0))
