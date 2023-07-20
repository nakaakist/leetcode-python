# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
picked = 4


def guess(num: int) -> int:
    if num > picked:
        return -1
    elif num < picked:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        def _guess(n, min, max):
            r = guess(n)
            if r == 0:
                return n
            elif r == -1:
                return _guess((min + n - 1) // 2, min, n - 1)
            else:
                return _guess((max + n + 1) // 2, n + 1, max)

        return _guess(n, 1, 2**31 - 1)


print(Solution().guessNumber(3))
