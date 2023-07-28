from bisect import bisect_left
from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()

        prefix = ""
        result = []
        for c in searchWord:
            prefix += c
            start = bisect_left(products, prefix)

            suggestions = []
            for i in range(start, min(len(products), start + 3)):
                p = products[i]
                if p.startswith(prefix):
                    suggestions.append(p)

            result.append(suggestions)

        return result


print(
    Solution().suggestedProducts(
        products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        searchWord="mouse",
    )
)
print(Solution().suggestedProducts(products=["havana"], searchWord="havana"))
