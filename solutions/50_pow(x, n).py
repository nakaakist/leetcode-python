class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        curr = x
        n_bit = abs(n)
        while n_bit > 0:
            ans *= curr if n_bit & 1 == 1 else 1
            curr *= curr
            n_bit >>= 1

        return ans if n >= 0 else 1.0 / ans


print(Solution().myPow(0.1, 10))
print(Solution().myPow(0, 1))
print(Solution().myPow(2, -4))
print(Solution().myPow(-2, -2))
print(Solution().myPow(0.00001, 100000))
