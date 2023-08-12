class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_p = {}
        mapped_words = set()
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        for p, w in zip(pattern, words):
            if p in map_p:
                if w != map_p[p]:
                    return False
            else:
                if w in mapped_words:
                    return False
                mapped_words.add(w)
                map_p[p] = w

        return True
