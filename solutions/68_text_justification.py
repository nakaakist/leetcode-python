from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def get_words_in_line(i):
            required_length = 0
            j = i
            l_words = []
            for j in range(i, len(words)):
                w = words[j]
                required_length += len(w) if i == j else len(w) + 1
                if required_length <= maxWidth:
                    l_words.append(w)
                else:
                    break

            return l_words

        def construct_line(l_words, is_end):
            if is_end:
                l_str = " ".join(l_words)
                return l_str + " " * (maxWidth - len(l_str))

            if len(l_words) == 1:
                return l_words[0] + " " * (maxWidth - len(l_words[0]))

            num_gaps = len(l_words) - 1
            num_chars = sum([len(w) for w in l_words])
            base_spaces_in_gap, gaps_for_extra_space = divmod(
                maxWidth - (num_chars), num_gaps
            )
            l_str = ""
            for i, w in enumerate(l_words):
                l_str += w
                if i < len(l_words) - 1:
                    l_str += " " * base_spaces_in_gap
                if i < gaps_for_extra_space:
                    l_str += " "

            return l_str

        result = []
        i = 0
        while True:
            l_words = get_words_in_line(i)
            i += len(l_words)

            if i == len(words):
                result.append(construct_line(l_words, True))
                return result
            else:
                result.append(construct_line(l_words, False))


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
