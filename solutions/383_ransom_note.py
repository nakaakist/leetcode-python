from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c_counts = Counter(magazine)

        for c in ransomNote:
            if c_counts[c] == 0:
                return False
            else:
                c_counts[c] -= 1

        return True


print(Solution().canConstruct(ransomNote="a", magazine="b"))
print(Solution().canConstruct(ransomNote="aa", magazine="aab"))
