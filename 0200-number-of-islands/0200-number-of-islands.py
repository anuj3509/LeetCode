class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()     # tro track the visited portion
        islands = 0
        
        # empty grid
        if not grid:
            return 0
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0],[0, 1],[0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) and 
                        grid[r][c] == "1" and (r, c) not in visited):   # this is land
                        q.append((r, c))
                        visited.add((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands