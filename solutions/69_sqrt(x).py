class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        nl, nr = 0, x
        while nl < nr - 1:
            mid = (nl + nr) // 2
            sq = mid**2
            if x < sq:
                nr = mid
            elif x > sq:
                nl = mid
            else:
                return mid

        return nl


print(Solution().mySqrt(10))
print(Solution().mySqrt(0))
print(Solution().mySqrt(2))
print(Solution().mySqrt(16))
