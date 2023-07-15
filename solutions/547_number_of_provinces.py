from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = [False] * len(isConnected)

        def visit_all_cities_in_province(start: int):
            stack = [start]
            while stack:
                c = stack.pop()
                for i in range(len(isConnected)):
                    if not seen[i] and isConnected[c][i]:
                        seen[i] = True
                        stack.append(i)

        n_provinces = 0
        for i in range(len(isConnected)):
            if seen[i]:
                continue

            visit_all_cities_in_province(i)
            n_provinces += 1

        return n_provinces


print(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
