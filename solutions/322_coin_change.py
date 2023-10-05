from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        MAX = float("inf")

        @cache
        def num_coins(amount: int):
            if amount == 0:
                return 0
            elif amount < 0:
                return -1

            n_rest_min = MAX
            for c in coins:
                n_rest = num_coins(amount - c)
                n_rest_min = min(n_rest_min, n_rest) if n_rest >= 0 else n_rest_min

            return n_rest_min + 1 if n_rest_min < MAX else -1

        return num_coins(amount)


print(Solution().coinChange(coins=[1, 2, 5], amount=11))
print(Solution().coinChange(coins=[2, 1], amount=3))
print(Solution().coinChange(coins=[2], amount=3))
print(Solution().coinChange(coins=[186, 419, 83, 408], amount=6249))
