class Solution:
    def climbStairs(self, n: int) -> int:
        c, p = 1, 0
        for _ in range(n):
            c, p = c + p, c

        return c


print(Solution().climbStairs(1))
print(Solution().climbStairs(3))
print(Solution().climbStairs(2))
