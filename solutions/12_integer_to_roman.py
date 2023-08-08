class Solution:
    values = {
        0: {
            1: "I",
            5: "V",
        },
        1: {
            1: "X",
            5: "L",
        },
        2: {
            1: "C",
            5: "D",
        },
        3: {1: "M", 5: ""},
    }

    def intToRoman(self, num: int) -> str:
        roman = ""
        for s in range(3, -1, -1):
            d = (num // 10**s) % 10
            if d != 4 and d != 9:
                roman += (self.values[s][5]) * (d // 5) + self.values[s][1] * (d % 5)
            elif d == 4:
                roman += self.values[s][1] + self.values[s][5]
            else:
                roman += self.values[s][1] + self.values[s + 1][1]

        return roman


print(Solution().intToRoman(3))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
