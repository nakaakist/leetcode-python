from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max_sum = float("-inf")
        max_sum = float("-inf")
        curr_min_sum = float("inf")
        min_sum = float("inf")
        s = 0
        for i, n in enumerate(nums):
            s += n
            curr_max_sum = max(n, n + curr_max_sum)
            max_sum = max(max_sum, curr_max_sum)

            if i == 0:
                continue
            curr_min_sum = min(n, n + curr_min_sum)
            min_sum = min(min_sum, curr_min_sum)

        return max(max_sum, s - min_sum)


print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))
print(Solution().maxSubarraySumCircular([5, -3, 5]))
print(Solution().maxSubarraySumCircular([1, 2, 3]))
print(Solution().maxSubarraySumCircular([-3, -2, -3]))
