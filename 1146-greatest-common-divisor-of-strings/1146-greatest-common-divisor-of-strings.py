class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if concatinating of str1 + str2 is not same as concatinating of str2 + str1
        if str1 + str2 != str2 + str1:
            return ""

        # if both strings are same
        if len(str1) == len(str2):
            return str1

        # if str2 is a smaller string 
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        
        # else if str1 is a smaller string
        return self.gcdOfStrings(str1, str2[len(str1):])