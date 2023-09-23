from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        msb, lsb = 0, 0
        for n in nums:
            tmp = msb
            msb = (~n & msb) | (lsb & n)
            lsb = (~n & lsb) | (n & ((~lsb) & (~tmp)))

        return lsb


print(Solution().singleNumber([2, 2, 2, 3]))
print(Solution().singleNumber([2, 44, 2, 2, 1, 1, 1, 3, 3, 3]))
print(Solution().singleNumber([3, 2, 2, 2, 1, 1, 1]))
