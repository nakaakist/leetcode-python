from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        ans = []

        i = 0
        while i < len(intervals):
            merged_start, merged_end = intervals[i]
            j = i
            while j < len(intervals) - 1 and intervals[j + 1][0] <= merged_end:
                j += 1
                merged_end = max(merged_end, intervals[j][1])

            ans.append([merged_start, merged_end])
            i = j + 1

        return ans


print(Solution().merge(intervals=[[2, 6], [1, 3], [8, 10], [15, 18]]))
print(Solution().merge(intervals=[[1, 4], [4, 5]]))
print(Solution().merge(intervals=[[1, 4], [2, 3]]))
