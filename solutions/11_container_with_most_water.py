from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i_l = 0
        i_r = len(height) - 1

        max_area = 0
        while i_l < i_r:
            h_l = height[i_l]
            h_r = height[i_r]
            area = (i_r - i_l) * min(h_l, h_r)
            if area > max_area:
                max_area = area

            if h_l >= h_r:
                while height[i_r] <= h_r and i_l < i_r:
                    i_r -= 1
            else:
                while height[i_l] <= h_l and i_l < i_r:
                    i_l += 1

        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution().maxArea([1, 1]))
print(Solution().maxArea([1, 2, 4, 3]))
