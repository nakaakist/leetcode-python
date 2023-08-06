from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i_write = 0
        last = None
        has_dup_last = False
        for i, n in enumerate(nums):
            if last == n and has_dup_last:
                continue

            nums[i_write] = n
            i_write += 1

            if last == n:
                has_dup_last = True
            else:
                last = n
                has_dup_last = False

        return i_write


nums = [0, 1, 2, 2, 2, 3, 4, 4, 5]
k = Solution().removeDuplicates(nums)
print(nums[:k])
