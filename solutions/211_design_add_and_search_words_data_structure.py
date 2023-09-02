class WordDictionary:
    SENTINEL = "_"

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr[self.SENTINEL] = {}

    def search(self, word: str) -> bool:
        node_to_search = [self.trie]
        for c in word + self.SENTINEL:
            tmp = []
            while node_to_search:
                curr = node_to_search.pop()
                if c == ".":
                    for k in curr:
                        tmp.append(curr[k])
                else:
                    if c in curr:
                        tmp.append(curr[c])
            if len(tmp) == 0:
                return False

            node_to_search = tmp

        return True


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))
