class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        memo = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for p1 in range(1, l1 + 1):
            for p2 in range(1, l2 + 1):
                if text1[p1 - 1] == text2[p2 - 1]:
                    memo[p1][p2] = memo[p1 - 1][p2 - 1] + 1
                else:
                    memo[p1][p2] = max(memo[p1 - 1][p2], memo[p1][p2 - 1])

        return memo[l1][l2]


print(Solution().longestCommonSubsequence("abcde", "bce"))
