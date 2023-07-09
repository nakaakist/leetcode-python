from typing import Generator, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leaves(self, root: Optional[TreeNode]) -> Generator[int, None, None]:
        if not root:
            return

        if not root.left and not root.right:
            yield root.val

        yield from self.leaves(root.left)
        yield from self.leaves(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = list(self.leaves(root1))
        l2 = list(self.leaves(root2))

        return l1 == l2


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3, n1, n2)
n4 = TreeNode(4)
n5 = TreeNode(5, n3, n4)

m1 = TreeNode(2)
m2 = TreeNode(2)
m3 = TreeNode(3, m1, m2)
m4 = TreeNode(4)
m5 = TreeNode(10, m3, m4)


print(Solution().leafSimilar(n5, m5))
