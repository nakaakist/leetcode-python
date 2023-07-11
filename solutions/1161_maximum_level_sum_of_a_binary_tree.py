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
        max = (0, float("-inf"))

        queue = deque([root, None])
        level = 1
        sum = 0
        while queue:
            n = queue.popleft()
            if not n:
                if sum > max[1]:
                    max = (level, sum)

                if not queue:
                    break

                queue.append(None)
                level += 1
                sum = 0
                continue

            sum += n.val

            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        return max[0]


n2 = TreeNode(2000)
n1 = TreeNode(1, None, n2)
n3 = TreeNode(3, n1)
n7 = TreeNode(7)
n6 = TreeNode(3)
n4 = TreeNode(2)
n5 = TreeNode(1, n6, n4)


print(Solution().maxLevelSum(n5))
