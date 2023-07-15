from collections import defaultdict
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        while stack:
            r = stack.pop()
            ks = rooms[r]
            for k in ks:
                if not seen[k]:
                    seen[k] = True
                    stack.append(k)

        return all(seen)


print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
