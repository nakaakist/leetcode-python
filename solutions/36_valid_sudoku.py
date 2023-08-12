from typing import List


class Solution:
    SIZE = 9
    CELL_SIZE = 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_nums = [{} for _ in range(self.SIZE)]
        col_nums = [{} for _ in range(self.SIZE)]
        sqr_nums = [{} for _ in range(self.SIZE)]

        def get_sqr_idx(i, j):
            return self.CELL_SIZE * (i // self.CELL_SIZE) + j // self.CELL_SIZE

        def set_num(i, j, n):
            if n in row_nums[i]:
                return False
            if n in col_nums[j]:
                return False
            i_sqr = get_sqr_idx(i, j)
            if n in sqr_nums[i_sqr]:
                return False

            row_nums[i][n] = True
            col_nums[j][n] = True
            sqr_nums[i_sqr][n] = True
            return True

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if board[i][j] == ".":
                    continue
                r = set_num(i, j, int(board[i][j]))
                if not r:
                    return False

        return True


print(
    Solution().isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

print(
    Solution().isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
