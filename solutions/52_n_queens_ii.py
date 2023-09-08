from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0

        def place(i: int, j: int, placed: List[int]):
            for k, l in enumerate(placed):
                if k == i or l == j:
                    return False
                if abs(k - i) == abs(l - j):
                    return False
            placed.append(j)
            return True

        def remove(placed):
            placed.pop()

        def backtrack(i: int, placed: List[int]):
            nonlocal ans
            if i == n:
                ans += 1
                return

            for j in range(n):
                if place(i, j, placed):
                    backtrack(i + 1, placed)
                    remove(placed)

        backtrack(0, [])

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
