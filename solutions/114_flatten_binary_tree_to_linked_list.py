from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]
        n_prev = None
        while stack:
            n = stack.pop()
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)

            if n_prev:
                n_prev.left = None
                n_prev.right = n
            n_prev = n
