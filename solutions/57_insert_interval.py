from bisect import bisect_left
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        i = bisect_left(intervals, newInterval)
        intervals.insert(i, newInterval)

        ans = []
        for i in range(len(intervals)):
            if not ans or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1] = [ans[-1][0], max(intervals[i][1], ans[-1][1])]

        return ans


print(Solution().insert(intervals=[], newInterval=[5, 7]))
