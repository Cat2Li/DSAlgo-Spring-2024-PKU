class TreeNode(object):

    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None


n = int(input())

nodes = [TreeNode() for _ in range(n)]
for i in range(n):
    left, right = map(int, input().split())
    if left != -1:
        nodes[i].left = nodes[left]
        nodes[left].parent = nodes[i]
    if right != -1:
        nodes[i].right = nodes[right]
        nodes[right].parent = nodes[i]

root = nodes[0]
while root.parent:
    root = root.parent


def get_depth(node, depth):
    if node is None:
        return depth
    return max(get_depth(node.left, depth + 1),
               get_depth(node.right, depth + 1))


depth = get_depth(root, -1)


def is_leaf(node):
    return node.left is None and node.right is None


leaves_cnt = sum([is_leaf(node) for node in nodes])
print(depth, leaves_cnt)
