from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            n, v = stack.pop()
            if n.left is None and n.right is None and v == targetSum:
                return True

            if n.left:
                stack.append((n.left, v + n.left.val))
            if n.right:
                stack.append((n.right, v + n.right.val))

        return False
