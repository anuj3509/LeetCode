class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumofsquares(n)

            if n == 1:
                return True
        return False    # return false when encounter a loop and that loop is not with 1

    
    def sumofsquares(self, n: int) -> int:
        output = 0

        while n:    # stop when the unit digit is 0
            digit = n % 10      # getting digit at unit's place
            digit = digit ** 2  # squaring
            output += digit     # adding to the sum of squares
            n = n // 10         # find next digit
        return output