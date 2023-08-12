from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h = len(matrix)
        w = len(matrix[0])

        result = []
        depth = 0
        i = 0
        j = 0
        d = "r"
        while len(result) < w * h:
            result.append(matrix[i][j])
            if d == "r":
                if j == w - depth - 1:
                    d = "d"
                    i += 1
                else:
                    j += 1
            elif d == "d":
                if i == h - depth - 1:
                    d = "l"
                    j -= 1
                else:
                    i += 1
            elif d == "l":
                if j == depth:
                    d = "u"
                    i -= 1
                else:
                    j -= 1
            else:
                if i == depth + 1:
                    d = "r"
                    j += 1
                    depth += 1
                else:
                    i -= 1

        return result


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
