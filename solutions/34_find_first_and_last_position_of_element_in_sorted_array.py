from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        il = bisect_left(nums, target)
        ir = bisect_right(nums, target)

        if il >= len(nums) or nums[il] != target:
            return [-1, -1]
        else:
            return [il, ir - 1]


print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(Solution().searchRange(nums=[7, 7, 7, 8, 8, 10], target=7))
print(Solution().searchRange(nums=[7, 7, 7, 8, 8, 10], target=10))
print(Solution().searchRange(nums=[7, 7, 7, 8, 8, 10], target=2))
print(Solution().searchRange(nums=[7, 7, 7, 8, 8, 10], target=12))
