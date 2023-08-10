class Solution:
    def convert(self, s: str, numRows: int) -> str:
        converted = [""] * numRows

        is_down = True
        row = 0
        for c in s:
            converted[row] += c
            if is_down:
                row += 1
                if row >= numRows - 1:
                    is_down = False
                    row = numRows - 1
            else:
                row -= 1
                if row <= 0:
                    is_down = True
                    row = 0

        return "".join(converted)


print(Solution().convert("PAYPALISHIRING", 3))
print(Solution().convert("A", 1))
print(Solution().convert("AB", 1))
