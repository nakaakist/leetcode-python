class Solution:
    def isPalindrome(self, s: str) -> bool:
        def norm_alphanumeric(c: str):
            code = ord(c)
            # number
            if code >= 48 and code <= 57:
                return c
            # lowercase
            elif code >= 97 and code <= 122:
                return c
            # uppercase
            elif code >= 65 and code <= 90:
                return c.lower()
            else:
                return None

        i_l = 0
        i_r = len(s) - 1
        while i_l <= i_r:
            c_l = None
            while c_l is None and i_l < i_r:
                c_l = norm_alphanumeric(s[i_l])
                i_l += 1
            c_r = None
            while c_r is None and i_l < i_r:
                c_r = norm_alphanumeric(s[i_r])
                i_r -= 1

            if c_l != c_r:
                return False

        return True
