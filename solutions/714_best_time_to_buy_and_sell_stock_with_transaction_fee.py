from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)
        hold = -prices[0]
        free = 0

        for i in range(1, size):
            tmp = hold
            hold = max(tmp, free - prices[i])
            free = max(free, prices[i] - fee + tmp)

        return free


print(Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
print(Solution().maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))
