from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def min_hour_to_eat_all(k):
            return sum([ceil(p / k) for p in piles])

        k_min = 1
        k_max = max(piles)

        while k_min < k_max:
            k_mid = (k_min + k_max) // 2
            h_mid = min_hour_to_eat_all(k_mid)

            if h_mid <= h:
                k_max = k_mid
            else:
                k_min = k_mid + 1

        return k_max


print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
print(Solution().minEatingSpeed(piles=[10], h=9))
