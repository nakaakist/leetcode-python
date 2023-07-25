class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for _ in range(30):
            da = a & 1
            db = b & 1
            dc = c & 1

            if dc == 1:
                if da == 0 and db == 0:
                    flips += 1
            else:
                if da == 1:
                    flips += 1
                if db == 1:
                    flips += 1

            a = a >> 1
            b = b >> 1
            c = c >> 1

        return flips


print(Solution().minFlips(a=2, b=6, c=5))
print(Solution().minFlips(a=4, b=2, c=7))
