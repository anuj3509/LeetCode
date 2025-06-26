class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s) 
        count = 0 
        total = 0 # initialize the binary value so far
        power = 1 # start with 2^0 for the LSB
        for i in range(n - 1, -1, -1): 
            if s[i] == '0': 
                count += 1 
            else:
                # check if including this 1 doesn't exceed k
                if total + power <= k: 
                    total += power 
                    count += 1 
            power <<= 1 # move to the next MSB
            if power > k: 
                break 
        count += s[:i].count('0')
        return count 
