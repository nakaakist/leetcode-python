from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        SENTINEL = "_"

        trie = {}
        for w in words:
            curr = trie
            for c in w + SENTINEL:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]

        n_row = len(board)
        n_col = len(board[0])
        visited = [[False] * n_col for _ in range(n_row)]
        result = []

        def dfs(i, j, curr_trie, s):
            nonlocal result, visited
            cb = board[i][j]
            if cb not in curr_trie:
                return

            visited[i][j] = True
            next_s = s + cb
            next_trie = curr_trie[cb]

            if SENTINEL in next_trie:
                del next_trie[SENTINEL]
                result.append(next_s)

            for dv, dh in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                v, h = i + dv, j + dh
                if v < 0 or v >= n_row or h < 0 or h >= n_col or visited[v][h]:
                    continue
                dfs(v, h, next_trie, next_s)
            visited[i][j] = False

            if not next_trie:
                del curr_trie[cb]

        for i in range(n_row):
            for j in range(n_col):
                dfs(i, j, trie, "")

        return result


print(
    Solution().findWords(
        board=[
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        words=["oath", "pea", "eat", "rain"],
    )
)
print(Solution().findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))
print(Solution().findWords(board=[["a"]], words=["a"]))
print(Solution().findWords(board=[["a", "a"]], words=["aaa"]))
