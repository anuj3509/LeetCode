class Solution:
    def secondHighest(self, s: str) -> int:
        num = set()
        for char in s:
            if char in '0123456789':
                num.add(char)
        
        if len(num) >= 2 and int(sorted(num)[-2]) != int(sorted(num)[-1]):
            return int(sorted(num)[-2])
        else:
            return -1
        # return int(sorted(num)[-2]) if int(sorted(num)[-2]) != int(sorted(num)[-1]) else -1