class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        
        for i in range(len(s) - 1, -1, -1):
            # skip spaces at the end
            while (s[i] == " " and i >= 0):
                i -= 1
            
            length = 0
            while (s[i] != " ") and i >= 0:
                length += 1
                i -= 1
            return length

        