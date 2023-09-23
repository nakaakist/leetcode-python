from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def is_on_line(p1: List[int], p2: List[int], p_test: List[int]) -> int:
            return (p_test[0] - p1[0]) * (p_test[1] - p2[1]) - (p_test[0] - p2[0]) * (
                p_test[1] - p1[1]
            ) == 0

        l_p = len(points)
        ans = 1
        for i in range(l_p):
            for j in range(i + 1, l_p):
                n_on_line = 0
                for k in range(l_p):
                    if is_on_line(points[i], points[j], points[k]):
                        n_on_line += 1
                ans = max(ans, n_on_line)

        return ans


print(Solution().maxPoints([[1, 1], [2, 2], [3, 3]]))
