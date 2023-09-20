class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans |= ((n >> i) & 1) << (31 - i)

        return ans


print(Solution().reverseBits(0b00000010100101000001111010011100))
print(Solution().reverseBits(0))
