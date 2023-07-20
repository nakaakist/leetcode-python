from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        il_max = candidates - 1
        l = costs[: il_max + 1]
        ir_min = max(candidates, len(costs) - candidates)
        r = costs[ir_min:]
        total_cost = 0

        heapify(l)
        heapify(r)

        for _ in range(k):
            l_cand = l[0] if len(l) > 0 else float("inf")
            r_cand = r[0] if len(r) > 0 else float("inf")

            if l_cand <= r_cand:
                heappop(l)
                total_cost += l_cand
                if il_max < ir_min - 1:
                    il_max += 1
                    heappush(l, costs[il_max])
            else:
                heappop(r)
                total_cost += r_cand
                if il_max < ir_min - 1:
                    ir_min -= 1
                    heappush(r, costs[ir_min])

        return total_cost


print(Solution().totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4))
print(Solution().totalCost([1, 2, 4, 1], 3, 3))
print(
    Solution().totalCost(
        [
            28,
            35,
            21,
            13,
            21,
            72,
            35,
            52,
            74,
            92,
            25,
            65,
            77,
            1,
            73,
            32,
            43,
            68,
            8,
            100,
            84,
            80,
            14,
            88,
            42,
            53,
            98,
            69,
            64,
            40,
            60,
            23,
            99,
            83,
            5,
            21,
            76,
            34,
        ],
        32,
        12,
    )
)
