from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        i_l = 0
        l_min = float("inf")
        for i_r in range(len(nums)):
            sum += nums[i_r]
            while sum >= target:
                l_min = min(l_min, i_r - i_l + 1)
                sum -= nums[i_l]
                i_l += 1

        return 0 if l_min == float("inf") else l_min


print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(target=4, nums=[1, 4, 4]))
print(Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
