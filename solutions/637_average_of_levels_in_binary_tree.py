from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])

        ans = []
        while queue:
            queue.append(None)  # add sentinel
            total, count = 0, 0
            while queue[0] is not None:
                n = queue.popleft()
                total += n.val
                count += 1
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            ans.append(total / count)
            queue.popleft()  # remove sentinel

        return ans
