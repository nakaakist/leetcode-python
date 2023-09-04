from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        uniq_candidates = list(set(candidates))
        uniq_candidates.sort(reverse=True)

        result = []

        def backtracking(curr, sum_so_far, i_first):
            if target == sum_so_far:
                result.append(curr[:])
                return

            remaining = target - sum_so_far
            n_first = uniq_candidates[i_first]
            if remaining >= n_first:
                curr.append(n_first)
                backtracking(curr, sum_so_far + n_first, i_first)
                curr.pop()

            if i_first < len(candidates) - 1:
                backtracking(curr, sum_so_far, i_first + 1)

        backtracking([], 0, 0)

        return result
