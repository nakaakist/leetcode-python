class Solution:
    def trailingZeroes(self, n: int) -> int:
        n_5 = 0
        n_2 = 0

        def count_factor(i: int, f: int) -> int:
            ans = 0
            while i % f == 0:
                ans += 1
                i //= f
            return ans

        for i in range(1, n + 1):
            n_5 += count_factor(i, 5)
            n_2 += count_factor(i, 2)

        return min(n_5, n_2)


print(Solution().trailingZeroes(3))
print(Solution().trailingZeroes(5))
