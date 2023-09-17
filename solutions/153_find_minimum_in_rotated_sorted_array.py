from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find(il: int, ir: int) -> int:
            if il >= ir:
                return nums[ir]

            i_mid = (il + ir) // 2
            if nums[i_mid] < nums[ir]:
                return find(il, i_mid)
            else:
                return find(i_mid + 1, ir)

        return find(0, len(nums) - 1)


print(Solution().findMin([3, 4, 5, 1, 2]))
print(Solution().findMin([1]))
print(Solution().findMin([1, 2, 3, 4, 5]))
print(Solution().findMin([5, 1, 2, 3, 4]))
print(Solution().findMin([5, 1, 2, 3]))
