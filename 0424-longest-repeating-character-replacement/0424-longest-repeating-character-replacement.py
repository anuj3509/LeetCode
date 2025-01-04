class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # count = {}  # to count occurences of each result
        # l = 0
        # res = 0     # to store the max size of the sliding window

        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)

        #     while (r-l+1) - max(count.values()) > k:
        #         count[s[l]] -= 1
        #         l += 1
        #     res = max(res, r-l+1)
        # return res

        # Slightly optimized solution
        # Earlier it was O(26*n), after this it would be O(n)

        count = {}  # to count occurences of each result
        l = 0
        res = 0     # to store the max size of the sliding window
        maxf = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res