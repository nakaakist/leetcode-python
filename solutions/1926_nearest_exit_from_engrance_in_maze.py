from collections import defaultdict, deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n_rows, n_cols = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = "+"
        queue = deque([(entrance, 0)])

        while queue:
            (_x, _y), step = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = _x + dx, _y + dy
                if x < 0 or x >= n_rows or y < 0 or y >= n_cols:
                    continue
                if maze[x][y] == "+":
                    continue

                if x == 0 or x == n_rows - 1 or y == 0 or y == n_cols - 1:
                    return step + 1

                maze[x][y] = "+"
                queue.append(((x, y), step + 1))

        return -1


print(
    Solution().nearestExit(
        [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
    )
)
print(
    Solution().nearestExit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0])
)
print(Solution().nearestExit([[".", "+"]], [0, 0]))
