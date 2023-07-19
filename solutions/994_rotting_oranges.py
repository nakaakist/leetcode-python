from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])

        n_fresh = 0
        queue = deque([])
        for i in range(n_row):
            for j in range(n_col):
                v = grid[i][j]
                if v == 1:
                    n_fresh += 1
                elif v == 2:
                    queue.append(((i, j), 0))

        if n_fresh == 0:
            return 0

        while queue:
            (_i, _j), step = queue.popleft()

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i, j = _i + di, _j + dj
                if i < 0 or i >= n_row or j < 0 or j >= n_col:
                    continue
                if grid[i][j] != 1:
                    continue

                grid[i][j] = 2
                n_fresh -= 1
                queue.append(((i, j), step + 1))
                if n_fresh == 0:
                    return step + 1

        return -1


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(Solution().orangesRotting([[0, 2]]))
