from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(lambda: [])
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return groups.values()


print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
