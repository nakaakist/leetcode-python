from heapq import heappop, heappush
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        added_so_far = [-1] * len(nums1)

        q = [(nums1[0] + nums2[0], 0, 0)]
        added_so_far[0] = 0

        def push(i1: int, i2: int):
            if i1 < len(nums1) and i2 < len(nums2) and added_so_far[i1] < i2:
                heappush(q, (nums1[i1] + nums2[i2], i1, i2))
                added_so_far[i1] = i2

        ans = []
        for _ in range(k):
            if len(q) == 0:
                break
            _sum, i1, i2 = heappop(q)
            ans.append([nums1[i1], nums2[i2]])
            push(i1 + 1, i2)
            push(i1, i2 + 1)

        return ans


print(Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
print(Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
print(Solution().kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))
