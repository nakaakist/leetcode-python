class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift


print(Solution().rangeBitwiseAnd(left=5, right=7))
print(Solution().rangeBitwiseAnd(left=1, right=1))
