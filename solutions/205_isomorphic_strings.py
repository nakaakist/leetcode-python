class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        mapped = set()
        for c_s, c_t in zip(s, t):
            if c_s in map:
                if c_t != map[c_s]:
                    return False
            else:
                if c_t in mapped:
                    return False
                map[c_s] = c_t
                mapped.add(c_t)

        return True


print(Solution().isIsomorphic(s="egg", t="add"))
print(Solution().isIsomorphic(s="badc", t="baba"))
