from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(curr, remain):
            if len(curr) == len(nums):
                result.append(curr[:])
                return
            for i, n in enumerate(remain):
                curr.append(n)
                backtracking(curr, remain[:i] + remain[i + 1 :])
                curr.pop()

        backtracking([], nums)

        return result
