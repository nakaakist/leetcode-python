from typing import Optional, Tuple

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.pathLength = 0

        def dfs(node, goLeft, steps):
            if node:
                self.pathLength = max(self.pathLength, steps)
                if goLeft:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)

        dfs(root, False, 0)
        dfs(root, True, 0)
        return self.pathLength


n2 = TreeNode(2)
n1 = TreeNode(1, None, n2)
n3 = TreeNode(3, n1)
n7 = TreeNode(7)
n6 = TreeNode(6, n7, n2)
n4 = TreeNode(4, None, n6)
n5 = TreeNode(5, None, n4)


print(Solution().longestZigZag(n5))
