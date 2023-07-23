from collections import deque
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

        queue = deque(self.mapping[digits[0]])

        for d in digits[1:]:
            curr_letters = self.mapping[d]
            n = len(queue)

            for _ in range(n):
                comb = queue.popleft()
                for l in curr_letters:
                    queue.append(comb + l)

        return list(queue)


print(Solution().letterCombinations("23"))
