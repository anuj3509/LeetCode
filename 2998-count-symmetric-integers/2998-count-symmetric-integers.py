class Solution:
  def countSymmetricIntegers(self, low: int, high: int) -> int:
    
    def isSymmetricInteger(num: int) -> bool:

        # check if the first digit is equal to the second digit in a 2-digit number
        if num >= 10 and num <= 99:
            return num // 10 == num % 10

        # check if the sum of first and second digit is equal to the 
        # sum of third and fourth digit in a 4-digit number
        if num >= 1000 and num <= 9999:
            left = num // 100
            right = num % 100
            return left // 10 + left % 10 == right // 10 + right % 10

        return False    # 3 digit numbers are not symmetric

    return sum(isSymmetricInteger(num) for num in range(low, high + 1))