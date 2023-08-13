from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        count = Counter(s)

        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return False

        return True


print(Solution().isAnagram(s="rat", t="car"))
print(Solution().isAnagram(s="anagram", t="nagaram"))
