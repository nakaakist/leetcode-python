from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max = float("-inf")
        max_level = 0
        queue = deque([root])

        level = 1
        while queue:
            sum = 0
            n_nodes = len(queue)
            for _ in range(n_nodes):
                n = queue.popleft()
                sum += n.val
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

            if sum > max:
                max = sum
                max_level = level

            level += 1

        return max_level


n2 = TreeNode(2000)
n1 = TreeNode(1, None, n2)
n3 = TreeNode(3, n1)
n7 = TreeNode(7)
n6 = TreeNode(3)
n4 = TreeNode(2)
n5 = TreeNode(1, n6, n4)


print(Solution().maxLevelSum(n5))
