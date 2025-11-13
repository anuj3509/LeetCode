class Solution:
    def maxOperations(self, s: str) -> int:
        # scan in reverse order and keep track of groups of zeros, and track 1s that follow

        zero_segments = 0
        res = 0

        for i in reversed(range(len(s))):
            if s[i] == '0':
                if (i == len(s) - 1 or s[i+1] == '1'):
                    zero_segments += 1
            else:
                res += zero_segments         
        return res