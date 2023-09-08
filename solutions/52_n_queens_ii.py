class Solution:
    def totalNQueens(self, n: int) -> int:
        placed = [[False] * n for _ in range(n)]
        attacked = [[False] * n for _ in range(n)]
        ans = 0

        def idx_to_grid(idx):
            return divmod(idx, n)

        def place(i, j, placed, attacked):
            if attacked[i][j]:
                return False
            for k in range(n):
                if placed[k][j]:  # vertical
                    return False
                if placed[i][k]:  # horizontal
                    return False
                if (
                    j + k - i >= 0 and j + k - i < n and placed[k][j + k - i]
                ):  # diagonal
                    return False
                if (
                    j - k + i >= 0 and j - k + i < n and placed[k][j - k + i]
                ):  # diagonal
                    return False
            placed[i][j] = True
            for k in range(n):
                attacked[k][j] = True
                attacked[i][k] = True
                if j + k - i >= 0 and j + k - i < n:
                    attacked[k][j + k - i] = True
                if j - k + i >= 0 and j - k + i < n:
                    attacked[k][j - k + i] = True

            return True

        def remove(i, j, placed, attacked):
            placed[i][j] = False
            for k in range(n):
                attacked[k][j] = False
                attacked[i][k] = False
                if j + k - i >= 0 and j + k - i < n:
                    attacked[k][j + k - i] = False
                if j - k + i >= 0 and j - k + i < n:
                    attacked[k][j - k + i] = False

        def backtrack(idx, placed, attacked, n_to_place):
            nonlocal ans
            i, j = idx_to_grid(idx)
            if n_to_place == 0:
                ans += 1
                return
            if idx == n**2:
                return

            place_res = place(i, j, placed, attacked)
            if place_res:
                backtrack(idx + 1, placed, attacked, n_to_place - 1)
                remove(i, j, placed, attacked)
            backtrack(idx + 1, placed, attacked, n_to_place)

        backtrack(0, placed, attacked, n)

        return ans


print(Solution().totalNQueens(1))
print(Solution().totalNQueens(2))
print(Solution().totalNQueens(3))
print(Solution().totalNQueens(4))
print(Solution().totalNQueens(5))
print(Solution().totalNQueens(6))
print(Solution().totalNQueens(7))
print(Solution().totalNQueens(8))
