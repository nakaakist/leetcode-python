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
        queue = deque([root, None])
        curr = None
        while queue:
            prev, curr = curr, queue.popleft()
            if not curr:
                if not prev:
                    break
                result.append(prev.val)
                queue.append(None)
                continue

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return result


n2 = TreeNode(2)
n1 = TreeNode(1, None, n2)
n3 = TreeNode(3, n1)
n7 = TreeNode(7)
n6 = TreeNode(6, n7, n2)
n4 = TreeNode(4, None, n6)
n5 = TreeNode(5, n3, n4)


print(Solution().rightSideView(n5))
