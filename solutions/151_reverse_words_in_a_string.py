class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  world   hello  "))
