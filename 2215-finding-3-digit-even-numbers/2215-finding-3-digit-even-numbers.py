class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        n = len(digits)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue  # ensuring all digits are distinct
                    a, b, c = digits[i], digits[j], digits[k]
                    if a == 0:
                        continue  # number isn't starting with 0
                    if c % 2 != 0:  # even
                        continue  
                    num = 100 * a + 10 * b + c
                    result.add(num)

        return sorted(result)