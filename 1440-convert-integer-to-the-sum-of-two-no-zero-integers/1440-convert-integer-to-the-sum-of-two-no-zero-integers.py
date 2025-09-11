class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        firstNum = 0
        secondNum = n
        while firstNum < n and secondNum > 0:
            if str(firstNum).count("0") == 0 and str(secondNum).count("0") == 0:
                return [firstNum, secondNum]
            else:
                firstNum += 1
                secondNum -= 1