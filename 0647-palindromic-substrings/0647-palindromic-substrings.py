class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0     # count of palindromic substrings

        for i in range(len(s)):
            # l = r = i         -> odd length palindromes
            res += self.countpalindromes(s, i, i)
            
            # l, r = i, i + 1   -> even length palindromes
            res += self.countpalindromes(s, i, i+1)
        return res


    def countpalindromes(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res