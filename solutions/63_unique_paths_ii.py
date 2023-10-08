from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                nl = obstacleGrid[i][j - 1] if j > 0 else 0
                nt = obstacleGrid[i - 1][j] if i > 0 else 0
                obstacleGrid[i][j] += nl + nt

        return obstacleGrid[m - 1][n - 1]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]))
