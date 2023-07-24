class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        memo = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1 + 1):
            memo[i][0] = i
        for j in range(l2 + 1):
            memo[0][j] = j

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    replaced = memo[i - 1][j - 1] + 1
                    deleted = memo[i - 1][j] + 1
                    inserted = memo[i][j - 1] + 1
                    memo[i][j] = min(replaced, deleted, inserted)

        return memo[l1][l2]


print(Solution().minDistance("abc", "ad"))
