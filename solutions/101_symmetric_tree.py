from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isInverted(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        s1 = [r1]
        s2 = [r2]

        while s1 or s2:
            n1 = s1.pop()
            n2 = s2.pop()
            if n1 is None and n2 is None:
                continue
            elif n1 is None or n2 is None:
                return False
            elif n1.val != n2.val:
                return False
            else:
                s1.extend([n1.left, n1.right])
                s2.extend([n2.right, n2.left])

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isInverted(root.left, root.right)


n1 = TreeNode(1)
n2 = TreeNode(1)
n3 = TreeNode(2, n1, n2)
n4 = TreeNode(1)
n5 = TreeNode(1)
n6 = TreeNode(2, n4, n5)
n7 = TreeNode(
    3,
    n3,
)

print(Solution().isSymmetric(n3))
