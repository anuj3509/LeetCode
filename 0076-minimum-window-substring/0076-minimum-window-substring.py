class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""
        # if len(s) < len(t) : return ""
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, reslen = [-1, -1] , float("infinity")
        # result has two pointers at -1 and -1 indicating empty and result length is set to
        # infinity because we need the minimum value for the length of the result

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update the new minimum result
                if (r-l+1) < reslen:
                    res = [l, r]
                    reslen = (r-l+1)
    
                # after finding the first substring which matches the condition, we will
                # start popping from the left to see if there is any shorter substring which
                # occurs later
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""
