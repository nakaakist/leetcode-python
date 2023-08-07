from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i_reachable = 0
        for i in range(len(nums)):
            if i > i_reachable:
                return False
            i_reachable = max(i_reachable, i + nums[i])

        return True
