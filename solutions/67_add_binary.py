class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na = 0
        for i, c in enumerate(a):
            if i > 0:
                na <<= 1
            if c == "1":
                na += 1
        nb = 0
        for i, c in enumerate(b):
            if i > 0:
                nb <<= 1
            if c == "1":
                nb += 1

        ns = na + nb
        if ns == 0:
            return "0"

        ans = ""
        while ns > 0:
            ans += "1" if ns & 1 == 1 else "0"
            ns >>= 1

        return "".join(reversed(ans))


print(Solution().addBinary("111", "1"))
