from collections import defaultdict
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = defaultdict(bool)
        keys[0] = True
        stack = [0]

        while stack:
            r = stack.pop()
            ks = rooms[r]
            for k in ks:
                if not keys[k]:
                    keys[k] = True
                    stack.append(k)

        for r in range(len(rooms)):
            if keys[r] == False:
                return False

        return True


print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
