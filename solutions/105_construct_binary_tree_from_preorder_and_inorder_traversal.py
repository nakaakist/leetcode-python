from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_pos_map = {v: i for i, v in enumerate(inorder)}

        def build(ip1, ip2, ii1, ii2):
            if ip1 > ip2:
                return None

            vc = preorder[ip1]
            iic = inorder_pos_map[vc]

            ll = iic - ii1

            root = TreeNode(vc)
            root.left = build(ip1 + 1, ip1 + ll, ii1, iic - 1)
            root.right = build(ip1 + ll + 1, ip2, iic + 1, ii2)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
