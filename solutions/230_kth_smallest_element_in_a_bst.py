from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1

        def inorder(n: Optional[TreeNode]):
            nonlocal count
            if not n:
                return None

            vl = inorder(n.left)
            if vl is not None:
                return vl

            if count == k:
                return n.val
            count += 1

            vr = inorder(n.right)
            if vr is not None:
                return vr

        return inorder(root)
