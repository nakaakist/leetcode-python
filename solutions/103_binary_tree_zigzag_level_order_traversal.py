from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        is_to_right = True
        result = []
        queue = deque([root])

        while queue:
            vals = []
            if is_to_right:
                queue.append(None)  # add sentinel
                while queue[0] is not None:
                    n = queue.popleft()
                    vals.append(n.val)
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                queue.popleft()  # remove sentinel
            else:
                queue.appendleft(None)  # add sentinel
                while queue[-1] is not None:
                    n = queue.pop()
                    vals.append(n.val)
                    if n.right:
                        queue.appendleft(n.right)
                    if n.left:
                        queue.appendleft(n.left)
                queue.pop()  # remove sentinel
            result.append(vals)
            is_to_right = not is_to_right

        return result
