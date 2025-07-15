class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False
        
        for ch in word:
            if not ch.isalnum():    # alphanumeric
                return False
            if ch in vowels:
                has_vowel = True
            elif ch.isalpha():  # consonants - alphabetic but not vowel
                has_consonant = True
        
        return has_vowel and has_consonant  # at least one vowel and one consonant

        # TC: O(n) ; SC: O(1)