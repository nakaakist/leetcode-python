from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n_row = len(board)
        n_col = len(board[0])

        islands = []

        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == "X" or board[i][j] == "V":
                    continue

                stack = [(i, j)]
                should_be_captured = True
                while stack:
                    k, l = stack.pop()
                    board[k][l] = "V"
                    if k == 0 or k == n_row - 1 or l == 0 or l == n_col - 1:
                        should_be_captured = False
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
                islands.append((i, j, should_be_captured))

        while islands:
            i, j, should_be_captured = islands.pop()
            stack = [(i, j)]
            while stack:
                k, l = stack.pop()
                board[k][l] = "X" if should_be_captured else "O"
                for dv, dh in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    m, n = k + dv, l + dh
                    if (
                        m >= 0
                        and m < n_row
                        and n >= 0
                        and n < n_col
                        and board[m][n] == "V"
                    ):
                        stack.append((m, n))
