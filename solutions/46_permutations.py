from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(curr):
            if len(curr) == len(nums):
                result.append(curr[:])
                return
            for n in nums:
                if n in curr:
                    continue
                curr.append(n)
                backtracking(curr)
                curr.pop()

        backtracking([])

        return result
