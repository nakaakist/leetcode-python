from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n

        return res


print(Solution().singleNumber([4, 1, 2, 1, 2]))
