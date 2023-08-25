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
            if n is None:
                return 0

            l = 1
            while n.left:
                n = n.left
                l += 1

            return l

        ll = max_level(root.left)
        lr = max_level(root.right)

        if ll == lr:
            return 1 + (2**ll - 1) + self.countNodes(root.right)
        else:
            return 1 + self.countNodes(root.left) + (2**lr - 1)
