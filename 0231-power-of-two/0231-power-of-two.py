class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return  n & (n-1) == 0

        # idea: if any number is a power of 2, only 1 digit in its binary representation would be '1',
        # rest all would be '0'. So taking logical and of the number and the number before would 
        # result in 0, which will only happen if a number is a power of 2