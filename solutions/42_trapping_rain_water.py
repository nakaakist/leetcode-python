from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        right_edges = []
        area = 0

        prev_h = 0
        for i, h in enumerate(height):
            if h < prev_h:
                right_edges.append((i, h, prev_h))
            elif h > prev_h:
                while right_edges:
                    j, bh, th = right_edges.pop()
                    width = i - j
                    height = h - bh if th > h else th - bh
                    area += width * height
                    if th > h:
                        right_edges.append((j, h, th))
                        break

            prev_h = h

        return area


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))
