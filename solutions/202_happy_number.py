class Solution:
    def isHappy(self, n: int) -> bool:
        def proceed(m: int):
            ans = 0
            while m > 0:
                m, d = divmod(m, 10)
                ans += d**2

            return ans

        seen = set()
        while n > 1 and not n in seen:
            seen.add(n)
            n = proceed(n)

        return n == 1
