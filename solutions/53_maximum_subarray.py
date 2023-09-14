from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum_sum = 0
        cum_sum_min = 0
        ans = float("-inf")
        for n in nums:
            cum_sum += n
            if cum_sum - cum_sum_min > ans:
                ans = cum_sum - cum_sum_min

            if cum_sum < cum_sum_min:
                cum_sum_min = cum_sum

        return ans


print(Solution().maxSubArray([-1]))
