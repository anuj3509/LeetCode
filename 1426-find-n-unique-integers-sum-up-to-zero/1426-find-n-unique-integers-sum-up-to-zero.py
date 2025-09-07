class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(2*i - n + 1 )
        return res