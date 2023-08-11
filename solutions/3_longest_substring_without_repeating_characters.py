class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i_start = 0
        l_max = 0
        seen_pos = {}
        for i_end in range(len(s)):
            if s[i_end] in seen_pos:
                i_start = max(i_start, seen_pos[s[i_end]] + 1)

            l_max = max(l_max, i_end - i_start + 1)
            seen_pos[s[i_end]] = i_end

        return l_max


print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring(""))
print(Solution().lengthOfLongestSubstring("aaa"))
print(Solution().lengthOfLongestSubstring("dvdf"))
print(Solution().lengthOfLongestSubstring("tmmzuxt"))
