from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        edges = defaultdict(lambda: [])
        for t, f in prerequisites:
            edges[f].append(t)
            indegree[t] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        ans = []
        while queue:
            n = queue.popleft()
            ans.append(n)
            for t in edges[n]:
                indegree[t] -= 1
                if indegree[t] == 0:
                    queue.append(t)

        if len(ans) == numCourses:
            return ans
        else:
            return []
