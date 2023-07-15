from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        conn_from_nodes = [[] for _ in range(n)]
        for c in connections:
            conn_from_nodes[c[0]].append(c)
            conn_from_nodes[c[1]].append(c)

        visited = [False] * n
        stack = [0]
        num_changed = 0
        while stack:
            node = stack.pop()
            visited[node] = True
            conns = conn_from_nodes[node]
            for [n1, n2] in conns:
                if n1 != node and not visited[n1]:
                    stack.append(n1)
                elif n2 != node and not visited[n2]:
                    num_changed += 1
                    stack.append(n2)

        return num_changed


print(Solution().minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
print(Solution().minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
print(Solution().minReorder(3, [[1, 0], [2, 0]]))
