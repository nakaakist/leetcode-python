from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0: 0, 1: 0}

        def min_cost(i):
            if i in memo:
                return memo[i]

            memo[i] = min(min_cost(i - 2) + cost[i - 2], min_cost(i - 1) + cost[i - 1])
            return memo[i]

        return min_cost(len(cost))


print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(Solution().minCostClimbingStairs([10, 15, 20]))
