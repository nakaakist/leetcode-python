from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        l_max = 0
        for i in range(len(matrix)):
            curr_seqs = 0
            max_seqs = 0
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    matrix[i][j] = int(matrix[i - 1][j]) + 1 if i > 0 else 1
                else:
                    matrix[i][j] = 0
                curr_seqs = curr_seqs + 1 if matrix[i][j] > l_max else 0
                max_seqs = max(max_seqs, curr_seqs)
            if max_seqs > l_max:
                l_max += 1

        return l_max**2


print(
    Solution().maximalSquare(
        matrix=[["1", "1", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"]]
    )
)
