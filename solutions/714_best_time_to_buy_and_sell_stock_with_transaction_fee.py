from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)
        hold = [-prices[0]] * (size)
        free = [0] * (size)

        for i in range(1, size):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], prices[i] - fee + hold[i - 1])

        return free[size - 1]


print(Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
print(Solution().maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))
