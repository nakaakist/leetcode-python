from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        ans = []
        start = nums[0]

        def flush(start: int, end: int):
            if start == end:
                ans.append(str(start))
            else:
                ans.append(f"{start}->{end}")

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue
            else:
                end = nums[i - 1]
                flush(start, end)
                start = nums[i]

        flush(start, nums[-1])
        return ans


print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
