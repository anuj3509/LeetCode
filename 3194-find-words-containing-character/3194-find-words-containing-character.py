class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        # for word in words:
        for i in range(len(words)):
            # for char in words[i]:
            if x in words[i]:
                res.append(i)
        return res