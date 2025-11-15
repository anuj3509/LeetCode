class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == "1":
                res = (res + (j - i + 1)) % MOD
                j += 1
            i = j + 1
        return res