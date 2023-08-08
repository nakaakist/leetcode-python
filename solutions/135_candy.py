from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            curr_r = ratings[i]
            prev_r = ratings[i - 1]
            prev_c = candies[i - 1]
            if curr_r > prev_r:
                candies[i] = prev_c + 1
            else:
                candies[i] = 1

            for j in range(i, 0, -1):
                if (candies[j - 1] <= candies[j]) and (ratings[j - 1] > ratings[j]):
                    print(candies)
                    candies[j - 1] += 1
                else:
                    break

        print(candies)
        return sum(candies)


print(Solution().candy([1, 0, 2]))
print(Solution().candy([1, 2, 2]))
print(Solution().candy([1, 3, 2, 2, 1]))
print(Solution().candy([1, 2, 3, 1, 0]))
# print(Solution().candy(list(range(12000, 0, -1))))
