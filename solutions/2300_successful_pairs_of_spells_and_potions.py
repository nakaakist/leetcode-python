from bisect import bisect_left
from math import ceil
from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()

        result = []
        for s in spells:
            min_p = ceil(success / s)
            n = len(potions) - bisect_left(potions, min_p)
            result.append(n)

        return result


print(Solution().successfulPairs([5, 1, 3], [1, 1, 1, 2, 3, 4, 5], 5))
print(Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16))
