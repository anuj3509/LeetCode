class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1   # shift n-th bit by i places get the i-th bit
            res = res | (bit << (31 - i))
        return res