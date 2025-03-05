class Solution:
    def coloredCells(self, n: int) -> int:
        
        # Math based approach [ TC: O(1) ]
        return 1 + 2*n*(n-1)

        # # TC: O(n)
        # res = 1
        # for i in range(n):      # 0 ... n-1
        #     res += (4*i)
        # return res