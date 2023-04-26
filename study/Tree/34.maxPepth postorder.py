from collections import deque


def maxDepthPostOrder(root):
    max_depth = 0

    if root is None:
        return max_depth
    
    left_depth = maxDepthPostOrder(root.left)
    right_depth = maxDepthPostOrder(root.right)
    max_depth = max(left_depth, right_depth) + 1

    return max_depth

class TreeNode:
    def __init__(self, left = None, right = None , value = None):
        self.left = left
        self.right = right
        self.value = value

root = TreeNode(value=3)
root.left = TreeNode(value=9)
root.right = TreeNode(value=20)
root.right.left = TreeNode(value=15)
root.right.right = TreeNode(value=8)

print(maxDepthPostOrder(root))