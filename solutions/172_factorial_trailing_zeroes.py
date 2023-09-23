class Solution:
    def trailingZeroes(self, n: int) -> int:
        def count_factor(f: int) -> int:
            _f = f
            ans = 0
            while n >= _f:
                ans += n // _f
                _f *= f

            return ans

        return count_factor(5)


print(Solution().trailingZeroes(3))
print(Solution().trailingZeroes(30))
