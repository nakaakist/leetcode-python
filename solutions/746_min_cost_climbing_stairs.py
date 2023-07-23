from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 = 0, 0

        for i in range(2, len(cost) + 1):
            curr = min(prev1 + cost[i - 2], prev2 + cost[i - 1])
            prev1 = prev2
            prev2 = curr

        return curr


print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(Solution().minCostClimbingStairs([10, 15, 20]))
