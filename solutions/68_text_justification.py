from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        l_start = 0
        num_chars_in_l = 0
        result = []

        for i, w in enumerate(words):
            num_chars_in_l += len(w)
            should_break_now = num_chars_in_l + (i - l_start) > maxWidth
            should_end_now = i == len(words) - 1
            if not should_break_now and not should_end_now:
                continue

            # calc line
            if should_break_now:
                l_end = i - 1
                num_gaps = l_end - l_start

                if num_gaps == 0:
                    result.append(
                        words[l_start] + " " * (maxWidth - len(words[l_start]))
                    )
                else:
                    l_str = ""
                    for j in range(l_start, l_end + 1):
                        base_spaces_in_gap, gaps_for_extra_space = divmod(
                            maxWidth - (num_chars_in_l - len(w)), num_gaps
                        )
                        l_str += words[j]
                        if j == l_end:
                            break
                        l_str += " " * base_spaces_in_gap
                        if j - l_start < gaps_for_extra_space:
                            l_str += " "

                    result.append(l_str)

                l_start = l_end + 1
                num_chars_in_l = len(w)

            # calc end line
            if should_end_now:
                l_str = ""
                for j in range(l_start, i + 1):
                    l_str += words[j]
                    if j < i:
                        l_str += " "
                l_str += " " * (maxWidth - len(l_str))
                result.append(l_str)

        return result


print(
    Solution().fullJustify(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
    )
)
print(
    Solution().fullJustify(
        words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16
    )
)
print(
    Solution().fullJustify(
        words=[
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        maxWidth=20,
    )
)
