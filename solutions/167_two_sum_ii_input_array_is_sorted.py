from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i_l = 0
        i_r = len(numbers) - 1

        while i_l < i_r:
            sum = numbers[i_l] + numbers[i_r]

            if sum == target:
                return [i_l + 1, i_r + 1]
            elif sum > target:
                i_r -= 1
            else:
                i_l += 1


print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))
print(Solution().twoSum(numbers=[5, 25, 75], target=100))
