from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        steps_to_down = [0] * n
        curr = 0
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                curr += 1
            else:
                curr = 0
            steps_to_down[i] = curr

        curr = steps_to_down[0] + 1
        ans = curr
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                curr = max(curr + 1, steps_to_down[i] + 1)
            else:
                curr = steps_to_down[i] + 1
            ans += curr

        return ans


print(Solution().candy([1, 0, 2]))
print(Solution().candy([1, 2, 2]))
print(Solution().candy([1, 3, 2, 2, 1]))
print(Solution().candy([1, 2, 3, 1, 0]))
print(Solution().candy(list(range(12000, 0, -1))))
