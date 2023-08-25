from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def max_level(n: Optional[TreeNode]):
            l = 0
            while n:
                n = n.left
                l += 1
            return l

        ll, lr = max_level(root.left), max_level(root.right)

        if ll == lr:
            return 2**ll + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + 2**lr
