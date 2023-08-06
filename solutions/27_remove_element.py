from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i_write = 0
        i_read = 0

        while i_read < len(nums):
            v = nums[i_read]
            i_read += 1

            if v == val:
                continue
            else:
                nums[i_write] = v
                i_write += 1

        return i_write


nums = [0, 1, 2, 2, 3, 0, 4, 2]
k = Solution().removeElement(nums, 1)
print(nums[:k])
