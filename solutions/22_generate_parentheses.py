from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(s: str, n_open: int, n_close: int):
            if n_open == n and n_close == n:
                ans.append(s)
                return

            if n_open < n:
                dfs(s + "(", n_open + 1, n_close)
            if n_close < n_open:
                dfs(s + ")", n_open, n_close + 1)

        dfs("", 0, 0)

        return ans


print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(3))
