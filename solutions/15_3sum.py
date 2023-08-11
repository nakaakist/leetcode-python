from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for i_l in range(len(nums) - 2):
            n_l = nums[i_l]
            if i_l > 0 and n_l == nums[i_l - 1]:
                continue

            i_m = i_l + 1
            i_r = len(nums) - 1

            while i_m < i_r:
                n_m = nums[i_m]
                n_r = nums[i_r]
                if i_m > i_l+1 and n_m == nums[i_m - 1]:
                    i_m += 1
                    continue
                elif i_r < len(nums) - 1 and n_r == nums[i_r + 1]:
                    i_r -= 1
                    continue

                s = n_l + n_m + n_r
                if s == 0:
                    result.append([n_l, n_m, n_r])

                if s > 0:
                    i_r -= 1
                else:
                    i_m += 1

        return result


print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum(nums=[0, 0, 0, 0, 0]))
