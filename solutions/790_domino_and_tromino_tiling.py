class Solution:
    MOD = 10**9 + 7

    def numTilings(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        memo_half_filled = {1: 0, 2: 2}

        def num_half_filled_tilings(n):
            if n in memo_half_filled:
                return memo_half_filled[n]

            memo_half_filled[n] = (
                num_half_filled_tilings(n - 1) + 2 * num_tilings(n - 2)
            ) % self.MOD

            return memo_half_filled[n]

        def num_tilings(n):
            if n in memo:
                return memo[n]

            memo[n] = (
                num_tilings(n - 1) + num_tilings(n - 2) + num_half_filled_tilings(n - 1)
            ) % self.MOD
            return memo[n]

        return num_tilings(n)


print(Solution().numTilings(1))
