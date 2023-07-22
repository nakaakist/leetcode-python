from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def find_peak(i_l, i_r) -> int:
            if i_l == i_r:
                return i_l

            i_mid = (i_l + i_r) // 2

            if nums[i_mid] > nums[i_mid + 1]:
                return find_peak(i_l, i_mid)
            else:
                return find_peak(i_mid + 1, i_r)

        return find_peak(0, len(nums) - 1)


print(Solution().findPeakElement([1, 2, 3, 1]))
