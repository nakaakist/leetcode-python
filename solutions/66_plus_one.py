from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add_one(i: int) -> List[int]:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    return [1] + digits
                else:
                    return add_one(i - 1)

        return add_one(len(digits) - 1)


print(Solution().plusOne([1, 2, 1]))
print(Solution().plusOne([9, 9, 9]))
