from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = [False] * len(isConnected)

        def visit_all_cities_in_province(start: int):
            stack = [start]
            while stack:
                c = stack.pop()
                connections = isConnected[c]
                for i, n in enumerate(connections):
                    if n == 0:
                        continue
                    if not seen[i]:
                        seen[i] = True
                        stack.append(i)

        def find_start():
            try:
                return seen.index(False)
            except:
                return -1

        n_provinces = 0
        while True:
            start = find_start()
            if start < 0:
                return n_provinces

            visit_all_cities_in_province(start)
            n_provinces += 1


print(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
