class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # if n == 2: return [1, 1]
        
        # if n > 2 and n % 5 == 0:
        #     return [11, n-11] 
        # else:
        #     return [1, n-1]

        firstNum = 0
        secondNum = n
        while firstNum < n and secondNum > 0:
            if str(firstNum).count("0")==0 and str(secondNum).count("0")==0:
                return [firstNum, secondNum]
            else:
                firstNum += 1
                secondNum -= 1