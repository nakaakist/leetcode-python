from math import ceil, floor
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        for i in range(ceil(size / 2)):
            for j in range(floor(size / 2)):
                positions = [
                    (i, j),
                    (j, size - 1 - i),
                    (size - 1 - i, size - 1 - j),
                    (size - 1 - j, i),
                ]
                p = positions[-1]
                prev = matrix[p[0]][p[1]]
                for p in positions:
                    matrix[p[0]][p[1]], prev = prev, matrix[p[0]][p[1]]
