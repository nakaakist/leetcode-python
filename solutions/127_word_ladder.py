from collections import deque
from string import ascii_lowercase
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        i_start = len(wordList) - 1

        word_idx_map = {w: i for i, w in enumerate(wordList)}
        nexts = [[] for _ in range(len(wordList))]
        i_end = -1
        for i, s in enumerate(wordList):
            if s == endWord:
                i_end = i
            for ic, c in enumerate(s):
                for l in ascii_lowercase:
                    if l == c:
                        continue
                    mut_s = s[:ic] + l + s[ic + 1 :]
                    if mut_s in word_idx_map:
                        nexts[i].append(word_idx_map[mut_s])

        dists = [-1] * len(wordList)
        dists[i_start] = 1
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

        return 0
