class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"

        if numerator % denominator == 0:
            return str(numerator // denominator)

        # perform division with positve numbers only, store the sign to append later
        if numerator * denominator < 0:
            sign = "-"
        else: 
            sign = ""
        
        num, den = abs(numerator), abs(denominator)
        res = sign + str(num // den) + "."
        num %= den
        remainders = {}     # hash map to keep the track of remainders we get

        while num:
            if num in remainders:
                i = remainders[num]
                return res[:i] + "(" + res[i:] + ")"
            remainders[num] = len(res)
            num *= 10
            res += str(num // den)
            num %= den

        return res