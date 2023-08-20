from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s_p = [p]
        s_q = [q]
        while s_p or s_q:
            n_p = s_p.pop()
            n_q = s_q.pop()

            if n_p is None or n_q is None:
                if n_p is None and n_q is None:
                    continue
                else:
                    return False
            elif n_p.val != n_q.val:
                return False

            s_p.extend([n_p.left, n_p.right])
            s_q.extend([n_q.left, n_q.right])

        return True
