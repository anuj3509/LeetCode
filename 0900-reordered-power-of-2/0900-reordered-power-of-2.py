class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        # idea: add all powers of 2 from 0 to 10^9 in an array, sort each numner in that array digitwise.
        # sort the number which we have digitwise
        # return true if this sorted number is in that array if sorted powers of 2

        num, arr = 2, []
        i = 0

        # this loop will add all powers of 2 in the array where each number is sorted digitwise
        while (num ** i) < (10 ** 9):
            arr.append(sorted(str(num ** i)))
            i += 1
            
        return sorted(str(n)) in arr    # true if the number is in the array