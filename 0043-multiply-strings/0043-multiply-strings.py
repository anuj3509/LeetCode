class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += digit             
                res[i + j + 1] += (res[i + j] // 10)    # to place carry in the next place
                res[i + j] = res[i + j] % 10        # to place only the unit's place digit
        
        # removing leading zeros
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])   # convert array to string
        return "".join(res)
