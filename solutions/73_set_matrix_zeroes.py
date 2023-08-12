from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(n_rows):
            for j in range(n_cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
