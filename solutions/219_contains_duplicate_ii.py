from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen_at = {}
        for i, n in enumerate(nums):
            if n in last_seen_at and i - last_seen_at[n] <= k:
                return True
            else:
                last_seen_at[n] = i

        return False
