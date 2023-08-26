from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float("inf")
        prevNode = None

        def inorder(n: Optional[TreeNode]):
            nonlocal ans, prevNode
            if not n:
                return

            inorder(n.left)
            if prevNode:
                ans = min(ans, n.val - prevNode.val)
            prevNode = n
            inorder(n.right)

        inorder(root)

        return ans
