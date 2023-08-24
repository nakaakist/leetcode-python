from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def paths(n: TreeNode):
            if n.left is None and n.right is None:
                return n.val, n.val, n.val
            elif n.left is None:
                rs, rw, rn = paths(n.right)
                return (n.val + max(rs, 0), n.val + max(rs, 0), max(rn, rs, rw))
            elif n.right is None:
                ls, lw, ln = paths(n.left)
                return (n.val + max(ls, 0), n.val + max(ls, 0), max(ln, ls, lw))
            else:
                ls, lw, ln = paths(n.left)
                rs, rw, rn = paths(n.right)
                return (
                    n.val + max(ls, rs, 0),
                    max(ls, 0) + n.val + max(rs,0),
                    max(ln, rn, ls, rs, lw, rw),
                )

        ls, lw, ln = paths(root)

        return max(ls, lw, ln)
