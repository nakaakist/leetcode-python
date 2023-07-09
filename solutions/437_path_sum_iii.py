from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        stack = [(root, [root.val])]
        n_patterns = 0
        while stack:
            n, sums_so_far = stack.pop()
            n_patterns += len([s for s in sums_so_far if s == targetSum])
            if n.left:
                stack.append(
                    (n.left, [s + n.left.val for s in sums_so_far] + [n.left.val])
                )
            if n.right:
                stack.append(
                    (n.right, [s + n.right.val for s in sums_so_far] + [n.right.val])
                )

        return n_patterns


n1 = TreeNode(3)
n2 = TreeNode(2)
n3 = TreeNode(3, n1, n2)
n4 = TreeNode(5)
n5 = TreeNode(5, n3, n4)


print(Solution().pathSum(n5, 10))
