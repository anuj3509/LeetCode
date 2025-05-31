class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n-1)
            res += 1
            # res += n % 2
            # n = n >> 1      # bit shift it to the right
        return res