from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prs_l = [0] * len(prices)
        p_min = float("inf")
        pr_curr = 0
        for i in range(len(prices)):
            p = prices[i]
            pr_curr = max(pr_curr, p - p_min)
            prs_l[i] = pr_curr
            p_min = min(p, p_min)

        prs_r = [0] * len(prices)
        p_max = float("-inf")
        pr_curr = 0
        for i in range(len(prices) - 1, -1, -1):
            p = prices[i]
            pr_curr = max(pr_curr, p_max - p)
            prs_r[i] = pr_curr
            p_max = max(p, p_max)

        ans = prs_r[0]
        for i in range(len(prices) - 1):
            ans = max(ans, prs_l[i] + prs_r[i + 1])

        return ans


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
