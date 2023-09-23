class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        cnt = right

        i = 1
        while cnt > 0:
            dl, ml = divmod(left, 2**i)
            dr, mr = divmod(right, 2**i)
            if dl == dr and (ml >= 2 ** (i - 1) and mr >= 2 ** (i - 1)):
                ans |= 2 ** (i - 1)
            cnt >>= 1
            i += 1

        return ans


print(Solution().rangeBitwiseAnd(left=5, right=7))
print(Solution().rangeBitwiseAnd(left=1, right=1))
