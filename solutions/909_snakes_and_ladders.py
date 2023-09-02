from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def seq_to_grid(i):
            _r, _c = divmod(i, n)
            if _r % 2 == 0:
                return n - 1 - _r, _c
            else:
                return n - 1 - _r, n - 1 - _c

        dist = [-1] * n**2

        queue = deque([0])
        dist[0] = 0
        while queue:
            i = queue.popleft()
            for next in range(i + 1, min(i + 7, n**2)):
                r, c = seq_to_grid(next)
                dest = next if board[r][c] == -1 else board[r][c] - 1
                if dist[dest] == -1:
                    dist[dest] = dist[i] + 1
                    queue.append(dest)

        return dist[n**2 - 1]
