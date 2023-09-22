class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            cnt += n & 1
            n >>= 1

        return cnt


print(Solution().hammingWeight(0b10001001001000000000000000001011))
print(Solution().hammingWeight(0b1))
