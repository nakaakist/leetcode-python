from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float("inf")
        curr_max_profit = 0

        for p in prices:
            if p < curr_min:
                curr_min = p
            elif p - curr_min > curr_max_profit:
                curr_max_profit = p - curr_min

        return curr_max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
