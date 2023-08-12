from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        s_counts = defaultdict(int)

        i_start = 0
        n_valid_chars_in_substr = 0
        l_substr_min = float("inf")
        i_start_min = 0
        i_end_min = 0
        for i_end in range(len(s)):
            c_end = s[i_end]
            if c_end in t_counts:
                s_counts[c_end] += 1
                if s_counts[c_end] <= t_counts[c_end]:
                    n_valid_chars_in_substr += 1

            while n_valid_chars_in_substr >= len(t):
                if i_end - i_start + 1 < l_substr_min:
                    l_substr_min = i_end - i_start + 1
                    i_start_min = i_start
                    i_end_min = i_end

                c_start = s[i_start]
                if c_start in t_counts:
                    s_counts[c_start] -= 1
                    if s_counts[c_start] < t_counts[c_start]:
                        n_valid_chars_in_substr -= 1

                i_start += 1

        return s[i_start_min : i_end_min + 1] if l_substr_min < float("inf") else ""


print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
print(Solution().minWindow(s="a", t="a"))
print(Solution().minWindow(s="a", t="aa"))
