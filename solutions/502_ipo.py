from heapq import heappop, heappush
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        zipped = [(c, p) for c, p in zip(capital, profits)]
        zipped.sort(key=lambda z: z[0], reverse=True)

        heap = []
        curr_cap = w
        for _i in range(k):
            while len(zipped) > 0 and zipped[len(zipped) - 1][0] <= curr_cap:
                _c, p = zipped.pop()
                heappush(heap, -p)

            if len(heap) == 0:
                break

            p_inv = heappop(heap)
            curr_cap -= p_inv

        return curr_cap


print(Solution().findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
print(Solution().findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))
print(Solution().findMaximizedCapital(k=1, w=10, profits=[1, 2, 3], capital=[0, 1, 1]))
