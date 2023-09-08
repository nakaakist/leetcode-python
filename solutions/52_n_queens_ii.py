from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0

        def idx_to_grid(idx):
            return divmod(idx, n)

        def place(i, j, placed, filled_rows, filled_cols):
            for k, l in placed:
                if k == i or l == j:
                    return False
                if abs(k - i) == abs(l - j):
                    return False
            placed.append((i, j))
            filled_rows.add(i)
            filled_cols.add(j)
            return True

        def remove(i, j, placed, filled_rows, filled_cols):
            placed.pop()
            filled_rows.remove(i)
            filled_cols.remove(j)

        def backtrack(idx, placed, filled_rows, filled_cols, n_to_place):
            nonlocal ans
            i, j = idx_to_grid(idx)
            if n_to_place == 0:
                ans += 1
                return
            if idx == n**2:
                return

            backtrack(idx + 1, placed, filled_rows, filled_cols, n_to_place)
            if i in filled_rows or j in filled_cols:
                return

            if place(i, j, placed, filled_rows, filled_cols):
                backtrack(idx + 1, placed, filled_rows, filled_cols, n_to_place - 1)
                remove(i, j, placed, filled_rows, filled_cols)

        backtrack(0, [], set(), set(), n)

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
