from itertools import chain
from typing import List


class Solution:
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        curr_letters = self.mapping[digits[-1]]
        if len(digits) == 1:
            return curr_letters

        prev = self.letterCombinations(digits[:-1])

        return list(chain.from_iterable([[p + l for p in prev] for l in curr_letters]))


print(Solution().letterCombinations("23"))
