from functools import cache
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def max_profit(i_start: int, k: int):
            if i_start >= len(prices) - 1 or k == 0:
                return 0

            min_p = prices[i_start]
            max_first_pr = 0
            ans = 0
            for i in range(i_start + 1, len(prices)):
                p = prices[i]
                min_p = min(p, min_p)
                if p - min_p > max_first_pr:
                    max_first_pr = p - min_p
                    ans = max(ans, max_profit(i + 1, k - 1) + max_first_pr)
            return ans

        return max_profit(0, k)


# print(Solution().maxProfit(k=2, prices=[2, 4, 1]))
print(Solution().maxProfit(k=2, prices=[3, 3, 5, 0, 0, 3, 1, 4]))
