from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)):
            if i == 0:
                continue
            prev = triangle[i - 1]
            curr = triangle[i]
            for i in range(len(curr)):
                p = min(
                    prev[i] if i < len(prev) else float("inf"),
                    prev[i - 1] if i > 0 else float("inf"),
                )
                curr[i] += p

        return min(triangle[-1])


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(Solution().minimumTotal([[-10]]))
