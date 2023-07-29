from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        curr_max = float("-inf")
        result = 0
        for x_min, x_max in points:
            if x_min <= curr_max:
                if x_max < curr_max:
                    curr_max = x_max
            else:
                result += 1
                curr_max = x_max

        return result


print(Solution().findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
print(Solution().findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))
print(
    Solution().findMinArrowShots(
        points=[[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
    )
)
