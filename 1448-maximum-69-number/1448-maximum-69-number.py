class Solution:
    def maximum69Number (self, num: int) -> int:
        res = ''
        flag = 0
        for number in str(num):
            if int(number) == 6 and flag == 0:
                number = str(int(number) + 3)
                flag = 1
            res += number
            # print(res)
        
        return int(res)