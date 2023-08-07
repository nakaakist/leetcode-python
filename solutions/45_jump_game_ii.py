from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n_steps = 0
        i_reachable = 0
        prev_i_reachable = 0
        while i_reachable < len(nums) - 1:
            next = 0
            for i in range(prev_i_reachable, i_reachable + 1):
                next = max(i + nums[i], next)

            prev_i_reachable = i_reachable
            i_reachable = next

            n_steps += 1

        return n_steps


print(Solution().jump([2, 3, 1, 1, 4]))
