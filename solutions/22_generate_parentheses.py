from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = [("", 0, 0)]

        while stack:
            s, n_open, n_close = stack.pop()
            if n_open == n and n_close == n:
                ans.append(s)
                continue

            if n_open < n:
                stack.append((s + "(", n_open + 1, n_close))
            if n_close < n_open:
                stack.append((s + ")", n_open, n_close + 1))

        return ans


print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(3))
