class Trie:
    STOP_CHAR = "_"

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        curr = self.tree
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        if self.STOP_CHAR not in curr:
            curr[self.STOP_CHAR] = {}

    def search(self, word: str) -> bool:
        curr = self.tree
        for c in word:
            if c not in curr:
                return False
            else:
                curr = curr[c]
        if self.STOP_CHAR not in curr:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree
        for c in prefix:
            if c not in curr:
                return False
            else:
                curr = curr[c]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))
