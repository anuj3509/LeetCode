class Solution:
    def coloredCells(self, n: int) -> int:
        
        # TC: O(n)
        res = 1
        for i in range(n):      # 0 ... n-1
            res += (4*i)
        return res