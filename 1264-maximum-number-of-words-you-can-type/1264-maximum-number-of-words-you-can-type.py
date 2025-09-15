class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        words = text.split()
        print(words)

        count = 0
        
        for word in words:
            for char in word:
                if char in brokenLetters:
                    break
            else:
                count += 1
        return count