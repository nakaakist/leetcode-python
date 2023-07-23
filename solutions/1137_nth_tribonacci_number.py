from collections import defaultdict


class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        def calc(n):
            if n == 0:
                return 0
            elif n in memo:
                return memo[n]
            else:
                ans = calc(n - 1) + calc(n - 2) + calc(n - 3)
                memo[n] = ans
                return ans

        return calc(n)


print(Solution().tribonacci(25))
