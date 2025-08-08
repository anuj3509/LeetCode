class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []

        for i in range(len(number)):
            if number[i] == digit:
                res.append( number[0: i] + number[i+1 :len(number)] )
                # print(number[:i-1])
        # print(res)
        return max(res)
