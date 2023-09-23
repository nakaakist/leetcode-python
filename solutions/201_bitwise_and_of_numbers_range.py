class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        cnt = right

        base = 1
        while cnt > 0:
            dl, ml = divmod(left, 2 * base)
            dr, mr = divmod(right, 2 * base)
            if dl == dr and (ml >= base and mr >= base):
                ans |= base
            cnt >>= 1
            base *= 2

        return ans


print(Solution().rangeBitwiseAnd(left=5, right=7))
print(Solution().rangeBitwiseAnd(left=1, right=1))
