class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()

        l = 0   #left pointer
        res = 0 #result variable to count the max size of the sliding window

        for r in range(len(s)):     #iterating the right pointer through the entire string
            while s[r] in charset:
                charset.remove(s[l])    #if duplicate encountered, keep removing leftmost value
                l += 1                  #increment left pointer
            charset.add(s[r])           #after all duplicates removed, add the right value
            res = max(res, r-l+1)       #keeps track of the max size of the sliding window
        
        return res
