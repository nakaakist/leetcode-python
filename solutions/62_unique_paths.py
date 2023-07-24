from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1] * n] * m

        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[m - 1][n - 1]
