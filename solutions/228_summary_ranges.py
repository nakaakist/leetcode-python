from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i_start = 0

        while i_start < len(nums):
            i_end = i_start
            while i_end < len(nums) - 1 and nums[i_end + 1] == nums[i_end] + 1:
                i_end += 1

            if i_start == i_end:
                ans.append(str(nums[i_start]))
            else:
                ans.append(f"{nums[i_start]}->{nums[i_end]}")
            i_start = i_end + 1

        return ans


print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
