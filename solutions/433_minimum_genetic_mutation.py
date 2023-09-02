from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def str_dist(s1: str, s2: str):
            return sum([c1 != c2 for c1, c2 in zip(s1, s2)])

        genes_set = set(bank)
        genes_set.add(startGene)
        uniq_genes = list(genes_set)

        nodes = list(range(len(uniq_genes)))
        nexts = [[] for _ in range(len(nodes))]
        i_start, i_end = -1, -1
        for i, s in enumerate(uniq_genes):
            if s == startGene:
                i_start = i
            if s == endGene:
                i_end = i
            for i2, s2 in enumerate(uniq_genes):
                if str_dist(s, s2) == 1:
                    nexts[i].append(i2)

        dists = [-1] * len(nodes)
        dists[i_start] = 0
        queue = deque([i_start])

        while queue:
            i = queue.popleft()
            if i == i_end:
                return dists[i_end]
            for i_next in nexts[i]:
                if dists[i_next] >= 0:
                    continue
                dists[i_next] = dists[i] + 1
                queue.append(i_next)

        return -1
