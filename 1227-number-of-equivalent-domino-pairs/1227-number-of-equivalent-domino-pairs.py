class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = collections.Counter()
        pairs = 0
        for a, b in dominoes:
            key = (a, b) if a <= b else (b, a)
            pairs += counts[key]
            counts[key] += 1
        return pairs
