from collections import deque
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        q1 = deque(nums1[0 : len(nums1) - len(nums2)])
        q2 = deque(nums2)

        i = 0
        while q1 or q2:
            if len(q1) == 0:
                next = q2.popleft()
            elif len(q2) == 0:
                next = q1.popleft()
            else:
                if q1[0] < q2[0]:
                    next = q1.popleft()
                else:
                    next = q2.popleft()

            nums1[i] = next
            i += 1
