from collections import defaultdict, deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n_rows, n_cols = len(maze), len(maze[0])
        visited = defaultdict(lambda: defaultdict(lambda: False))
        visited[entrance[0]][entrance[1]] = True
        queue = deque([(entrance, 0)])

        def visit_if_possible(x, y, step):
            if visited[x][y]:
                return False

            if (
                (x >= 0 and x < n_rows)
                and (y >= 0 and y < n_cols)
                and maze[x][y] == "."
            ):
                queue.append(((x, y), step + 1))
                visited[x][y] = True
                if x == 0 or x == n_rows - 1 or y == 0 or y == n_cols - 1:
                    return True

            return False

        while queue:
            (x, y), step = queue.popleft()
            print(x,y)
            if (
                visit_if_possible(x - 1, y, step)
                or visit_if_possible(x + 1, y, step)
                or visit_if_possible(x, y - 1, step)
                or visit_if_possible(x, y + 1, step)
            ):
                return step + 1

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