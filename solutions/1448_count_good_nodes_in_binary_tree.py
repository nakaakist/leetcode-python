import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def _goodNodes(max_ancestor, root) -> int:
            if not root:
                return 0
            if root.val >= max_ancestor:
                return (
                    _goodNodes(root.val, root.left)
                    + _goodNodes(root.val, root.right)
                    + 1
                )
            else:
                return _goodNodes(max_ancestor, root.left) + _goodNodes(
                    max_ancestor, root.right
                )

        return _goodNodes(float("-inf"), root)


n1 = TreeNode(3)
n2 = TreeNode(2)
n3 = TreeNode(3, n1, n2)
n4 = TreeNode(5)
n5 = TreeNode(5, n3, n4)


print(Solution().goodNodes(n5))
