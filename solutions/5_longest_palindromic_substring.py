from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        SENTINEL = "_"
        odd_candidates = deque(range(len(s)))
        even_candidates = deque(range(len(s) - 1))

        len_p = 0
        while odd_candidates:
            len_p += 1
            longest_odd_cand = odd_candidates[0]
            odd_candidates.append(SENTINEL)
            while odd_candidates[0] is not SENTINEL:
                i_center = odd_candidates.popleft()
                i_l, i_r = i_center - len_p, i_center + len_p
                if i_l < 0 or i_r >= len(s):
                    continue
                if s[i_l] != s[i_r]:
                    continue
                odd_candidates.append(i_center)
            odd_candidates.popleft()
        longest_odd = s[longest_odd_cand - len_p + 1 : longest_odd_cand + len_p]

        len_p = 0
        while even_candidates:
            len_p += 1
            longest_even_cand = even_candidates[0]
            even_candidates.append(SENTINEL)
            while even_candidates[0] is not SENTINEL:
                i_center = even_candidates.popleft()
                i_l, i_r = i_center - len_p + 1, i_center + len_p
                if i_l < 0 or i_r >= len(s):
                    continue
                if s[i_l] != s[i_r]:
                    continue
                even_candidates.append(i_center)
            even_candidates.popleft()
        longest_even = s[longest_even_cand - len_p + 2 : longest_even_cand + len_p]

        return longest_even if len(longest_even) > len(longest_odd) else longest_odd


print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
