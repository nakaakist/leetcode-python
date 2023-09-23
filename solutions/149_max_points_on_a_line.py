from collections import defaultdict
from math import atan2
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l_p = len(points)
        ans = 1
        for i in range(l_p):
            counts = defaultdict(lambda: 1)
            for j in range(l_p):
                if i == j:
                    continue
                rad = atan2(points[j][0] - points[i][0], points[j][1] - points[i][1])
                counts[rad] += 1
            if len(counts) > 0:
                ans = max(ans, max(counts.values()))

        return ans


print(Solution().maxPoints([[1, 1], [2, 2], [3, 3]]))
