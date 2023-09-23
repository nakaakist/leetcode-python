class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10

        il, ir = 0, len(digits) - 1
        while il < ir:
            if digits[il] != digits[ir]:
                return False
            il, ir = il + 1, ir - 1

        return True


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-1))
