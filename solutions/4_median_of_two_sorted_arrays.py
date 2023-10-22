from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_elem(s1: int, e1: int, s2: int, e2: int, k: int) -> int:
            if s1 > e1:
                return nums2[k - s1]
            if s2 > e2:
                return nums1[k - s2]

            nt = e1 - s1 + e2 - s2
            m1 = (e1 + s1) // 2
            m2 = (e2 + s2) // 2
            mv1 = nums1[m1]
            mv2 = nums2[m2]
            if k > m1 + m2:
                return (
                    find_elem(m1 + 1, e1, s2, e2, k)
                    if mv1 < mv2
                    else find_elem(s1, e1, m2 + 1, e2, k)
                )
            else:
                return (
                    find_elem(s1, e1, s2, m2 - 1, k)
                    if mv1 < mv2
                    else find_elem(s1, m1 - 1, s2, e2, k)
                )

        n_total = len(nums1) + len(nums2)

        if n_total % 2 == 0:
            lm = find_elem(0, len(nums1) - 1, 0, len(nums2) - 1, n_total // 2 - 1)
            gm = find_elem(0, len(nums1) - 1, 0, len(nums2) - 1, n_total // 2)
            return (lm + gm) / 2
        else:
            return find_elem(0, len(nums1) - 1, 0, len(nums2) - 1, n_total // 2)


print(Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2, 7]))
