class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        chartoword = {}
        wordtochar = {}

        for c, w in zip(pattern, words):
            if c in chartoword and chartoword[c] != w:
                return False
            if w in wordtochar and wordtochar[w] != c:
                return False
            chartoword[c] = w
            wordtochar[w] = c
        return True