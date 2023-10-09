from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def _is_interleave(i1: int, i2: int, i3: int) -> bool:
            if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
                return True

            if i1 < len(s1) and i3 < len(s3) and s3[i3] == s1[i1]:
                if _is_interleave(i1 + 1, i2, i3 + 1):
                    return True
            if i2 < len(s2) and i3 < len(s3) and s3[i3] == s2[i2]:
                if _is_interleave(i1, i2 + 1, i3 + 1):
                    return True

            return False

        return _is_interleave(0, 0, 0)


print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
