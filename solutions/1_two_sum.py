from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, n in enumerate(nums):
            if target - n in index_map:
                return [i, index_map[target - n]]
            index_map[n] = i
