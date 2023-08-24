from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_pos_map = {v: i for i, v in enumerate(inorder)}

        def build(ip1, ip2, ii1, ii2):
            if ip1 > ip2:
                return None

            vc = postorder[ip2]
            iic = inorder_pos_map[vc]

            ll = iic - ii1

            root = TreeNode(vc)
            root.left = build(ip1, ip1 + ll - 1, ii1, iic - 1)
            root.right = build(ip1 + ll, ip2 - 1, iic + 1, ii2)
            return root

        return build(0, len(postorder) - 1, 0, len(inorder) - 1)
