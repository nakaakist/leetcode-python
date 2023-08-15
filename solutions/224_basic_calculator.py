class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0

        def is_num(c):
            return c in "0123456789"

        while i < len(s):
            if s[i] in "(+-":
                stack.append(s[i])
            elif is_num(s[i]):
                i_start = i
                while i < len(s) - 1 and is_num(s[i + 1]):
                    i += 1
                stack.append(int(s[i_start : i + 1]))
            elif s[i] == ")":
                r = 0
                while stack[-1] != "(":
                    v = stack.pop()
                    op = "+" if stack[-1] == "(" else stack.pop()
                    r += v if op == "+" else -v
                stack.pop()  # remove '('
                stack.append(r)

            i += 1

        ans = 0
        while stack:
            v = stack.pop()
            op = "+" if not stack else stack.pop()
            ans += v if op == "+" else -v

        return ans


print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
print(Solution().calculate("-(1+(4+5+2)-3)-(6+8)"))
print(Solution().calculate("-(-1+(4-5+2)-3)-(6+8)"))
