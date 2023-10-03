from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        SENTINEL = "_"
        for w in wordDict:
            curr = trie
            for c in w + SENTINEL:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]

        @cache
        def _word_break(i: int):
            curr = trie
            j = i
            while j < len(s):
                if SENTINEL in curr:
                    next = _word_break(j)
                    if next:
                        return True
                if s[j] not in curr:
                    return False
                curr = curr[s[j]]
                j += 1

            return SENTINEL in curr

        return _word_break(0)


print(
    Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
)
print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(Solution().wordBreak(s="aaaaaaa", wordDict=["aaaa", "aa"]))
