from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        wl = len(words[0])
        w_counts = {}
        for w in words:
            w_counts[w] = w_counts[w] + 1 if w in w_counts else 1

        def find_for_offset(offset: int):
            seen_at = {w: [] for w in words}
            i_start = 0
            for i_end in range(len(s) // wl):
                w = s[wl * i_end + offset : wl * (i_end + 1) + offset]
                if w not in w_counts:
                    i_start = i_end + 1
                    continue
                else:
                    seen_at[w].append(i_end)

                    if (
                        len(seen_at[w]) > w_counts[w]
                        and seen_at[w][-w_counts[w] - 1] >= i_start
                    ):
                        i_start = seen_at[w][-w_counts[w] - 1] + 1

                    if i_end - i_start + 1 == len(words):
                        result.append(wl * i_start + offset)
                        i_start += 1

        for offset in range(wl):
            find_for_offset(offset)

        return result


print(Solution().findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
print(
    Solution().findSubstring(
        "wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]
    )
)
print(
    Solution().findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])
)
print(Solution().findSubstring(s="bbbbb", words=["bb", "bb"]))
