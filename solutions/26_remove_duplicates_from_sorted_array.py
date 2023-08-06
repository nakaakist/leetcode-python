from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i_write = 0
        last = None
        for i, n in enumerate(nums):
            if last == n:
                continue
            else:
                nums[i_write] = n
                last = n
                i_write += 1

        return i_write


nums = [0, 1, 2, 2, 3, 4, 4, 5]
k = Solution().removeDuplicates(nums)
print(nums[:k])
