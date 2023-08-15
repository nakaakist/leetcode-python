class Solution:
    def calculate(self, s: str) -> int:
        s += ")"
        stack = ["("]
        i = 0

        while i < len(s):
            if s[i] in "(+-":
                stack.append(s[i])
            elif s[i].isdigit():
                i_start = i
                while i < len(s) - 1 and s[i + 1].isdigit():
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

        return stack[0]


print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
print(Solution().calculate("-(1+(4+5+2)-3)-(6+8)"))
print(Solution().calculate("-(-1+(4-5+2)-3)-(6+8)"))
