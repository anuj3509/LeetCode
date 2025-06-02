class Solution:
    def getSum(self, a: int, b: int) -> int:        
        mask = 0xFFFFFFFF
        while b != 0:
            # carry now contains common bits of a and b, shifted left by 1
            carry = (a & b) << 1
            # sum without carry
            a = (a ^ b) & mask
            # prepare next iteration
            b = carry & mask

        # if a is in the range of a 32-bit positive int, return it directly;
        # otherwise compute two's complement to get the negative value
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)

        