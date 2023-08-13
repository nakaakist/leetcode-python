from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        for n in nums:
            if n - 1 not in num_set:
                curr = n
                while curr in num_set:
                    curr += 1

                ans = max(ans, curr - n)

        return ans


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(
    Solution().longestConsecutive(
        [-7, -1, 3, -9, -4, 7, -3, 2, 4, 9, 4, -9, 8, -7, 5, -1, -7]
    )
)
