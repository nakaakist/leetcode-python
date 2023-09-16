from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _search(i1: int, i2: int) -> int:
            if i1 == i2:
                if nums[i1] == target:
                    return i1
                else:
                    return -1

            i_mid = (i1 + i2) // 2
            n1 = nums[i1]
            n2 = nums[i2]
            n_mid = nums[i_mid]

            if n1 <= n_mid:
                if n1 <= target and target <= n_mid:
                    return _search(i1, i_mid)
                else:
                    return _search(i_mid + 1, i2)
            if n_mid <= n2:
                if n_mid <= target and target <= n2:
                    return _search(i_mid, i2)
                else:
                    return _search(i1, i_mid - 1)

        return _search(0, len(nums) - 1)


print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(Solution().search(nums=[3, 4, 5, 6, 7], target=5))
print(Solution().search(nums=[7, 4, 5, 6], target=8))
print(Solution().search(nums=[8, 9, 4, 5, 6], target=8))
print(Solution().search(nums=[8, 9, 4, 5, 6], target=4))
