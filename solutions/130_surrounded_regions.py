from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n_row = len(board)
        n_col = len(board[0])

        def dfs(i, j):
            if board[i][j] == "X" or board[i][j] == "E":
                return

            stack = [(i, j)]
            while stack:
                k, l = stack.pop()
                board[k][l] = "E"
                for dv, dh in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    m, n = k + dv, l + dh
                    if (
                        m >= 0
                        and m < n_row
                        and n >= 0
                        and n < n_col
                        and board[m][n] == "O"
                    ):
                        stack.append((m, n))

        for i in range(n_row):
            for j in [0, n_col - 1]:
                dfs(i, j)
        for i in [0, n_row - 1]:
            for j in range(n_col):
                dfs(i, j)
        for i in range(n_row):
            for j in range(n_col):
                v = board[i][j]
                if v == 'O':
                    board[i][j] = 'X'
                elif v == 'E':
                    board[i][j] = 'O'
