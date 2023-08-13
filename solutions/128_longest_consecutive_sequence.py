from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        upper = {}
        lower = {}
        ans = 1
        for n in nums:
            if n in lower or n in upper:
                continue

            # union
            if n - 1 in lower and n + 1 in upper:
                l = lower[n - 1]
                u = upper[n + 1]
                del lower[n - 1]
                del upper[n + 1]
            # lower extension
            elif n - 1 in lower:
                l = lower[n - 1]
                u = n
                del lower[n - 1]
            # upper extension
            elif n + 1 in upper:
                l = n
                u = upper[n + 1]
                del upper[n + 1]
            else:
                l = n
                u = n

            upper[l] = u
            lower[u] = l
            ans = max(ans, u - l + 1)

        return ans


# print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
# print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(
    Solution().longestConsecutive(
        [-7, -1, 3, -9, -4, 7, -3, 2, 4, 9, 4, -9, 8, -7, 5, -1, -7]
    )
)
