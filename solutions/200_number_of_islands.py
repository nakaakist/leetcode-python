from typing import List

# 1: unvisited land, 2: visited land, 0: water


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        num_islands = 0

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == "0" or grid[i][j] == "2":
                    continue

                num_islands += 1
                stack = [(i, j)]
                while stack:
                    k, l = stack.pop()
                    grid[k][l] = "2"
                    for dv, dh in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        m, n = k + dv, l + dh
                        if m < 0 or m >= n_row or n < 0 or n >= n_col:
                            continue
                        if grid[m][n] == "1":
                            grid[m][n] = "2"
                            stack.append((m, n))

        return num_islands
