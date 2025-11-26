class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])


        # top down solution with caching
        cache = [[[-1] * k for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, remainder):
            if r == rows - 1 and c == cols - 1:
                remainder = (remainder + grid[r][c]) % k
                return 0 if remainder else 1
            
            # out of bounds
            if r == rows or c == cols:
                return 0

            # caching case
            if cache[r][c][remainder] > -1:
                return cache[r][c][remainder]

            cache[r][c][remainder] = (
                dfs(r + 1, c, (remainder + grid[r][c]) % k) % MOD + 
                dfs(r, c + 1, (remainder + grid[r][c]) % k) % MOD
            ) % MOD
            return cache[r][c][remainder]
        
        return dfs(0, 0, 0)