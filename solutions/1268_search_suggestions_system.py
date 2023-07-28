from collections import OrderedDict
from typing import List


class OrderedTrie:
    STOP_CHAR = "_"

    def __init__(self) -> None:
        self.trie = OrderedDict([])

    def insert(self, word) -> None:
        node = self.trie
        for c in word + self.STOP_CHAR:
            if c not in node:
                node[c] = OrderedDict([])
                new_node = sorted(node.items(), key=lambda x: x[0], reverse=True)
                node.clear()
                node.update(new_node)

            node = node[c]

    def suggest(self, word) -> List[List[str]]:
        start_node = self.trie
        result = []
        prefix = ""
        for c in word:
            prefix += c

            if start_node is not None and c in start_node:
                start_node = start_node[c]
            else:
                start_node = None
                result.append([])
                continue

            stack = [(start_node, prefix)]
            suggestions = []
            while stack and len(suggestions) < 3:
                n, p = stack.pop()
                for l, child in n.items():
                    if l == self.STOP_CHAR:
                        suggestions.append(p)
                    else:
                        stack.append((child, p + l))

            result.append(suggestions)

        return result


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = OrderedTrie()
        for p in products:
            trie.insert(p)

        return trie.suggest(searchWord)


print(
    Solution().suggestedProducts(
        products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        searchWord="mouse",
    )
)
print(Solution().suggestedProducts(products=["havana"], searchWord="havana"))
