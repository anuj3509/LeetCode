class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = []
        l = 0

        for r in range(2, len(num)):
            substring = num[l] + num[r-1] + num[r]
            if int(substring) % 111 == 0:   # if all the digits are equal, then 111 would be a factor
                res.append(substring)
            l += 1
        return max(res) if res else ""