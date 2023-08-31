from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p_map = defaultdict(lambda: [])
        indegree = defaultdict(int)
        for f, t in prerequisites:
            p_map[f].append(t)
            indegree[t] += 1

        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)

        n_processed = 0
        while stack:
            n = stack.pop()
            n_processed += 1
            for t in p_map[n]:
                indegree[t] -= 1
                if indegree[t] == 0:
                    stack.append(t)

        return n_processed == numCourses
