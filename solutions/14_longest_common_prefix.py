from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1, len(strs)):
            s = strs[i]
            ans = ans[: len(s)]
            for j in range(len(ans)):
                if s[j] != ans[j]:
                    ans = ans[:j]
                    break

            if ans == "":
                break

        return ans


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
