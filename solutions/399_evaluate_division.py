from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        conn_map = defaultdict(lambda: [])
        for i in range(len(equations)):
            x, y = equations[i]
            v = values[i]
            conn_map[x].append((y, v))
            conn_map[y].append((x, 1 / v))

        def dfs(x, y, curr_val, visited):
            visited[x] = True
            if x == y and len(conn_map[x]) > 0:
                return curr_val

            conns = [c for c in conn_map[x] if not visited[c[0]]]
            if len(conns) == 0:
                return -1

            return max([dfs(x2, y, curr_val * v, visited) for x2, v in conns])

        return [dfs(x, y, 1, defaultdict(lambda: False)) for [x, y] in queries]


print(
    Solution().calcEquation(
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    )
)
