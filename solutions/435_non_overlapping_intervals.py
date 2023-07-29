from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])

        result = 0
        _, prev_i_max = intervals[0]
        for i_min, i_max in intervals[1:]:
            if prev_i_max <= i_min:
                prev_i_max = i_max
            else:
                prev_i_max = min(i_max, prev_i_max)
                result += 1

        return result


print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
print(Solution().eraseOverlapIntervals([[1, 2], [2, 3]]))
