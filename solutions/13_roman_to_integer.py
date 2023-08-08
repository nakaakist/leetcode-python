class Solution:
    map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            v = self.map[c]
            next_v = self.map[s[i + 1]] if i < len(s) - 1 else 0
            ans += v if v >= next_v else -v

        return ans


print(Solution().romanToInt("MCMXCIV"))
