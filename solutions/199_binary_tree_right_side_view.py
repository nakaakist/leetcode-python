from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])
        while queue:
            queue.append(None)  # add sentinel
            while queue[0] is not None:
                n = queue.popleft()
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            result.append(n.val)
            queue.popleft()  # remove sentinel

        return result


n2 = TreeNode(2)
n1 = TreeNode(1, None, n2)
n3 = TreeNode(3, n1)
n7 = TreeNode(7)
n6 = TreeNode(6, n7, n2)
n4 = TreeNode(4, None, n6)
n5 = TreeNode(5, n3, n4)


print(Solution().rightSideView(n5))
