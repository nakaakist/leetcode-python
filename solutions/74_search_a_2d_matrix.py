from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i_row = bisect_right(matrix, target, key=lambda r: r[0]) - 1
        row = matrix[i_row]
        i_col = bisect_left(row, target)
        return i_col < len(row) and row[i_col] == target


print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=10
    )
)
print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=1
    )
)
print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=8
    )
)
print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=68
    )
)
