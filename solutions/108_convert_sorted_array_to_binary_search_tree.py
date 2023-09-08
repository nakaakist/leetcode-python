from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def to_bst(i_start, i_end):
            if i_start > i_end:
                return None

            i_split = (i_start + i_end + 1) // 2
            root = TreeNode(nums[i_split])
            root.left = to_bst(i_start, i_split - 1)
            root.right = to_bst(i_split + 1, i_end)

            return root

        return to_bst(0, len(nums) - 1)
