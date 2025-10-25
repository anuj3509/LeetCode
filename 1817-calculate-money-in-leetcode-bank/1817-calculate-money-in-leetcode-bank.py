class Solution:
    def totalMoney(self, n: int) -> int:
        a = n // 7
        b = n % 7
        res = (a * (49 + 7*a))/2 + (b*(2*a + b + 1))/2
        return int(res)

        # sum of AP: n/2 * [2a + (n-1)d] or n/2 * [a + l]