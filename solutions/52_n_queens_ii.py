from typing import Set


class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0

        def place(
            i: int, j: int, cols: Set[int], diags: Set[int], anti_diags: Set[int]
        ):
            if j in cols or i - j in diags or i + j in anti_diags:
                return False
            cols.add(j)
            diags.add(i - j)
            anti_diags.add(i + j)
            return True

        def remove(
            i: int, j: int, cols: Set[int], diags: Set[int], anti_diags: Set[int]
        ):
            cols.remove(j)
            diags.remove(i - j)
            anti_diags.remove(i + j)

        def backtrack(i: int, cols: Set[int], diags: Set[int], anti_diags: Set[int]):
            nonlocal ans
            if i == n:
                ans += 1
                return

            for j in range(n):
                if place(i, j, cols, diags, anti_diags):
                    backtrack(i + 1, cols, diags, anti_diags)
                    remove(i, j, cols, diags, anti_diags)

        backtrack(0, set(), set(), set())

        return ans


print(Solution().totalNQueens(1))
print(Solution().totalNQueens(2))
print(Solution().totalNQueens(3))
print(Solution().totalNQueens(4))
print(Solution().totalNQueens(5))
print(Solution().totalNQueens(6))
print(Solution().totalNQueens(7))
print(Solution().totalNQueens(8))
print(Solution().totalNQueens(9))
