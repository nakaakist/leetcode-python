from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_no_edge = 0
        prev_edge = nums[0]

        for i in range(1, len(nums)):
            curr_no_edge = max(prev_edge, prev_no_edge)
            curr_edge = prev_no_edge + nums[i]

            prev_no_edge = curr_no_edge
            prev_edge = curr_edge

        return max(prev_no_edge, prev_edge)


print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([100, 2, 3, 100, 1, 100]))
print(Solution().rob([1]))
