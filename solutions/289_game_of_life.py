from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n_rows = len(board)
        n_cols = len(board[0])

        def get_cell_val(i, j):
            if i < 0 or j < 0 or i >= n_rows or j >= n_cols:
                return 0
            else:
                return board[i][j] & 1

        for i in range(n_rows):
            for j in range(n_cols):
                neighbors = 0
                for v in [-1, 0, 1]:
                    for h in [-1, 0, 1]:
                        if v == 0 and h == 0:
                            continue
                        neighbors += get_cell_val(i + h, j + v)

                if board[i][j] == 1:
                    if neighbors >= 2 and neighbors <= 3:
                        board[i][j] = 0b11
                else:
                    if neighbors == 3:
                        board[i][j] = 0b10

        for i in range(n_rows):
            for j in range(n_cols):
                board[i][j] = board[i][j] >> 1


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
Solution().gameOfLife(board)
print(board)
