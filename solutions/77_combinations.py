from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:
            return [list(range(1, k + 1))]
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        else:
            return [l + [n] for l in self.combine(n - 1, k - 1)] + self.combine(
                n - 1, k
            )


print(Solution().combine(3, 2))
