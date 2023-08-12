from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n_rows = len(board)
        n_cols = len(board[0])

        def get_cell_val(i, j):
            if i < 0 or j < 0 or i >= n_rows or j >= n_cols:
                return 0
            else:
                return board[i][j]

        result = [[0] * n_cols for _ in range(n_rows)]
        for i in range(n_rows):
            for j in range(n_cols):
                neighbors = 0
                for v in [-1, 0, 1]:
                    for h in [-1, 0, 1]:
                        if v == 0 and h == 0:
                            continue
                        neighbors += get_cell_val(i + h, j + v)

                if board[i][j] == 1:
                    result[i][j] = 0 if neighbors < 2 or neighbors > 3 else 1
                else:
                    result[i][j] = 1 if neighbors == 3 else 0

        for i in range(n_rows):
            for j in range(n_cols):
                board[i][j] = result[i][j]


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
Solution().gameOfLife(board)
print(board)
