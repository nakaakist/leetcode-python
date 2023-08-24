from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, root.val)]
        result = 0

        while stack:
            n, v = stack.pop()
            if n.left is None and n.right is None:
                result += v

            if n.left:
                stack.append((n.left, 10 * v + n.left.val))
            if n.right:
                stack.append((n.right, 10 * v + n.right.val))

        return result
