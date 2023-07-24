class Solution:
    MOD = 10**9 + 7

    def numTilings(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 2}
        memo_half_filled = {0: 0, 1: 0, 2: 2}

        if n <= 2:
            return memo[n]

        for i in range(3, n + 1):
            memo_half_filled[i] = (memo_half_filled[i - 1] + 2 * memo[i - 2]) % self.MOD
            memo[i] = (memo[i - 1] + memo[i - 2] + memo_half_filled[i - 1]) % self.MOD

        return memo[n]


print(Solution().numTilings(1000))
