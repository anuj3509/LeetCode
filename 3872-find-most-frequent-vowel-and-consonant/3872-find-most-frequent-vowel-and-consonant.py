class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        def isVowel(ch):
            str = "aeiouAEIOU"
            return (str.find(ch) != -1)

        max_vowel_count = max_consonants_count = 0
        char_map = {}
        
        for char in s:
            char_map[char] = 1 + char_map.get(char, 0)

        for key in char_map.keys():
            if isVowel(key):
                max_vowel_count = max(max_vowel_count, char_map.get(key))
            else:
                max_consonants_count = max(max_consonants_count, char_map.get(key))
        
        # print(max_vowel_count, max_consonants_count)
        return max_vowel_count + max_consonants_count