from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtrack(i, j, visited, i_word):
            c = word[i_word]
            if board[i][j] != c:
                return False
            elif i_word == len(word) - 1:
                return True

            for dv, dh in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                v, h = i + dv, j + dh
                if v < 0 or v >= m or h < 0 or h >= n or visited[v][h]:
                    continue
                visited[v][h] = True
                if backtrack(v, h, visited, i_word + 1):
                    return True
                visited[v][h] = False

            return False

        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]
                visited[i][j] = True
                if backtrack(i, j, visited, 0):
                    return True

        return False


print(
    Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
)
print(
    Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
)
