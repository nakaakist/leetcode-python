from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3, n1, n2)
n4 = TreeNode(4)
n5 = TreeNode(5, n3, n4)


print(Solution().maxDepth(n5))
