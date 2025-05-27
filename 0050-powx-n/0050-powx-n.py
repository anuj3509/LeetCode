class Solution:
    def myPow(self, x: float, n: int) -> float:

        # TC: O(log2(n))
        def helper(x, n):   # this function also avoids passing -ve exponent
            if n == 0:
                return 1
            if x == 0:
                return 0
        
            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res    # return (x * x^2 * x^2) if exponent is -ve

        res = helper(x, abs(n))
        return res if n >= 0 else 1/res