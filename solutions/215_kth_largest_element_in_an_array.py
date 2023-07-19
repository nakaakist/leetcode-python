import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            for n in nums:
                if n < pivot:
                    left.append(n)
                elif n == pivot:
                    mid.append(n)
                else:
                    right.append(n)

            if len(right) >= k:
                return quick_select(right, k)
            elif len(right) + len(mid) >= k:
                return pivot
            else:
                return quick_select(left, k - len(right) - len(mid))

        return quick_select(nums, k)


print(Solution().findKthLargest([1, 2, 3, 4], 2))
