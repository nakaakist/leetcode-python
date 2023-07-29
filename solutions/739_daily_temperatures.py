from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i_t, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j_t = stack.pop()
                result[j_t] = i_t - j_t

            stack.append(i_t)

        return result


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
