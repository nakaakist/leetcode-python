from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def _searchInsert(i1: int, i2: int):
            if i1 >= i2:
                return i1

            i_mid = (i1 + i2) // 2
            mid = nums[i_mid]

            if mid == target:
                return i_mid
            elif mid < target:
                return _searchInsert(i_mid + 1, i2)
            else:
                return _searchInsert(i1, i_mid)

        return _searchInsert(0, len(nums))


print(Solution().searchInsert(nums=[1, 3, 5, 6], target=5))
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=7))
print(Solution().searchInsert(nums=[1, 3, 5, 6, 6], target=-1))
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=-1))
print(Solution().searchInsert(nums=[1, 3], target=2))
