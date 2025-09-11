class Solution:
    def sortVowels(self, s: str) -> str:

        def isVowel(ch):
            str = "aeiouAEIOU"
            return (str.find(ch) != -1)

        res = ""
        vowels_list = [] # storing vowels

        # seperate out consonants and vowels and then sort vowels
        for char in s:
            if isVowel(char):
                vowels_list.append(char)
        vowels_list.sort()
        # print(vowels_list)

        i = 0   # to iterate the vowels list which we sorted above
        for char in s:
            if not isVowel(char):   
                res += char     # if consonant, keep the same in result
            else:
                res += str(vowels_list[i])   # if vowel, choose instead from the sorted list
                i += 1
        return res