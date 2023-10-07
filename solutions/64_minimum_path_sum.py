from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                vt = grid[i - 1][j] if i > 0 else float("inf")
                vl = grid[i][j - 1] if j > 0 else float("inf")
                grid[i][j] += min(vt, vl)

        return grid[m - 1][n - 1]


print(Solution().minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(Solution().minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
