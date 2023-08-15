class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        for c in s:
            if c in mapping:
                if len(stack) == 0:
                    return False
                c2 = stack.pop()
                if c2 != mapping[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
