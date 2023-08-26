from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    INF = 10**9

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def process(n: Optional[TreeNode]) -> (int, int, int):  # max, min, min_diff
            if not n:
                return -self.INF, self.INF, self.INF

            l_max, l_min, l_min_diff = process(n.left)
            r_max, r_min, r_min_diff = process(n.right)

            return (
                max(l_max, n.val, r_max),
                min(l_min, n.val, r_min),
                min(l_min_diff, r_min_diff, abs(n.val - l_max), abs(n.val - r_min)),
            )

        return process(root)[2]
