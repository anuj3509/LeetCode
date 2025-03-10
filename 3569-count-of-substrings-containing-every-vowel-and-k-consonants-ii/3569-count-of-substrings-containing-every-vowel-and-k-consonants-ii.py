class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        # Sliding window approach
        def atleastk(k):    # return total number of substring with atleast k consonants and all vowels
            vowel = defaultdict(int)
            non_vowel = 0
            res = 0
            l = 0
            for r in range(len(word)):
                if word[r] in "aeiou":
                    vowel[word[r]] += 1
                else:
                    non_vowel += 1
                while len(vowel) == 5 and non_vowel >= k:
                    res += (len(word) - r)
                    if word[l] in "aeiou":
                        vowel[word[l]] -= 1
                    else:
                        non_vowel -= 1
                    if vowel[word[l]] == 0:
                        vowel.pop(word[l])
                    l += 1
            return res

        return atleastk(k) - atleastk(k + 1)