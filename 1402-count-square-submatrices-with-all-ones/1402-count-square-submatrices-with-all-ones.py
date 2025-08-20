class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        total = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # first row/col can only form 1x1 square
                    else:
                        # if matrix[i][j] == 1, the size of the largest square ending at (i, j) 
                        # depends on its neighbors, i.e.,  dp[i][j] = 1 + min(top, left, top-left) if matrix[i][j] == 1
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    total += dp[i][j]

        return total


        # TC = SC = O(rows x cols)