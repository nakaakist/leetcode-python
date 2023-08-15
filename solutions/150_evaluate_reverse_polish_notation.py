from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }

        for t in tokens:
            if t in operations:
                y = stack.pop()
                x = stack.pop()
                r = operations[t](x, y)
                stack.append(r)
            else:
                stack.append(int(t))

        return stack[0]


print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
print(
    Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
