from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node and node.val != val:
            node = node.left if node.val > val else node.right

        return node


n1 = TreeNode(3)
n2 = TreeNode(2)
n3 = TreeNode(3, n1, n2)
n4 = TreeNode(5)
n5 = TreeNode(5, n3, n4)


print(Solution().searchBST(n5, 3).val)
