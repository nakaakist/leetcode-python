from math import gcd
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i_start in range(gcd(len(nums), k)):
            i = i_start
            n_for_next = nums[i]
            while True:
                i = (i + k) % len(nums)
                cache = nums[i]
                nums[i] = n_for_next
                if i == i_start:
                    break
                n_for_next = cache


a = [1, 2, 3, 4, 5]
Solution().rotate(a, 7)
print(a)
