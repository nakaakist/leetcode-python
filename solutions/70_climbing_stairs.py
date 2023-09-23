class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def _count(m: int):
            if m == 0:
                return 1
            elif m < 0:
                return 0

            if memo[m] >= 0:
                return memo[m]

            cnt = _count(m - 1) + _count(m - 2)
            memo[m] = cnt

            return cnt

        return _count(n)


print(Solution().climbStairs(3))
