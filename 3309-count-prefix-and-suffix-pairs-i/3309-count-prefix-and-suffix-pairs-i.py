class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        # TC: O(n^2 * L)
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                w1, w2 = words[i], words[j]
                L = len(w1)      # length of word at index i
                if w1 == w2[:L] and w1 == w2[-L:]:
                    res += 1
        return res