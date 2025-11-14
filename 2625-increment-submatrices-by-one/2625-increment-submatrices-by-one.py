class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff_mat = [[0] * (n + 1) for _ in range(n+1)]      # difference array but in 2D

        for r1, c1, r2, c2 in queries:
            diff_mat[r1][c1] += 1
            diff_mat[r1][c2 + 1] -= 1
            diff_mat[r2 + 1][c1] -= 1
            diff_mat[r2 + 1][c2 + 1] += 1
        
        res = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                # if else statements to prevent out of bounds error
                top = 0 if r == 0 else res[r-1][c]
                left = 0 if c == 0 else res[r][c-1]
                top_left = 0 if r == 0 or c == 0 else res[r-1][c-1]

                res[r][c] = diff_mat[r][c] + top + left - top_left
        
        return res