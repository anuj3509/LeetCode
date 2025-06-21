class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxLength = 0
        
        # for i in range(len(s)):
        #     seen = set()
        #     for j in range(i, len(s)):
        #         if s[j] not in seen:
        #             seen.add(s[j])
        #         else: 
        #             break
        #     maxLength = max(maxLength, len(seen))
        # return maxLength

                

        l = 0
        seen = set()
        length = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = max(length, len(seen))
        return length
            