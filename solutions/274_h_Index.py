from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for i in range(len(citations)):
            if i + 1 > citations[i]:
                return i

        return len(citations)


print(Solution().hIndex([3, 0, 6, 1, 5]))
print(Solution().hIndex([1, 3, 1]))
print(Solution().hIndex([3, 2, 1]))
print(Solution().hIndex([6, 3, 1]))
