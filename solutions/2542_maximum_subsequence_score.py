from heapq import heapify, heapreplace
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs.sort(key=lambda x: -x[1])

        top_k_heap = [p[0] for p in pairs[:k]]
        heapify(top_k_heap)
        top_k_sum = sum(top_k_heap)

        answer = top_k_sum * pairs[k - 1][1]

        for i in range(k, len(nums2)):
            n1, n2 = pairs[i]
            n1_popped = heapreplace(top_k_heap, n1)

            top_k_sum += n1 - n1_popped

            score = top_k_sum * n2

            answer = max(score, answer)

        return answer


print(Solution().maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3))
