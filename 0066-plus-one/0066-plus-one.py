class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]   # reversing the input array
        flag, i = 1, 0
        
        while flag:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    flag = 0
            else:
                digits.append(1)
                flag = 0
            i += 1
        return digits[::-1]