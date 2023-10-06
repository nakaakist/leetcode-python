from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_picked = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_picked[i] = max(max_picked[j] + 1, max_picked[i])

        return max(max_picked)


print(Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLIS(nums=list(range(10, 0, -1))))
print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
