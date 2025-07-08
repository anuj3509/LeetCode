class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            nxt = ''.join(chr(ord(c)+1) for c in word)
            word += nxt
        return word[k-1]
