from itertools import chain
from typing import List


class Solution:
    def combinations(self, min_i, k, n):
        if k == 1 and n < 10 and n >= min_i:
            return [[n]]
        elif k * min_i >= n:
            return []

        result = []
        for i in range(min_i, 10):
            result.extend([[i] + c for c in self.combinations(i + 1, k - 1, n - i)])
        return result

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.combinations(1, k, n)


print(Solution().combinationSum3(k=2, n=7))
