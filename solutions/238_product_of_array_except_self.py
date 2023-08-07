from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prod = 1
        for n in nums:
            prod *= n
            ans.append(prod)

        prod_right = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i - 1] * prod_right if i > 0 else prod_right
            n = nums[i]
            prod_right *= n

        return ans


print(Solution().productExceptSelf([1, 2, 3, 4]))
