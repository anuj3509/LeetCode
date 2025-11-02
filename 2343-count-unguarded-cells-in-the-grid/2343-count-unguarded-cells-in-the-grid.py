# class Solution:
#     def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
#         grid = [[0] * n for _ in range(m)]
#         # 0 = free, 1 = guard, 2 = wall, 3 = guardable

#         for r,c in guards:
#             grid[r][c] = 1
#         for r, c in walls:
#             grid[r][c] = 2

#         def mark_guarded(r, c):
#             for row in range(r+1, m):
#                 if grid[row][c] == 2 or grid[row][c] == 2:      # if cell is a wall or a guard, we break
#                     break
#                 grid[row][c] = 3
            
#             # doing the same thing as above in opposite direction
#             for row in reversed(range(0, r)):
#                 if grid[row][c] == 2 or grid[row][c] == 2:      # if cell is a wall or a guard, we break
#                     break
#                 grid[row][c] = 3
            
#             for col in range(c+1, n):
#                 if grid[r][col] == 2 or grid[r][col] == 2:      # if cell is a wall or a guard, we break
#                     break
#                 grid[r][col] = 3
            
#             # doing the same thing as above in opposite direction
#             for col in reversed(range(0, c)):
#                 if grid[r][col] == 2 or grid[r][col] == 2:      # if cell is a wall or a guard, we break
#                     break
#                 grid[r][col] = 3


#         for r, c in guards:
#             mark_guarded(r, c)
        
#         res = 0
#         for row in grid:
#             for n in row:
#                 if n == 0:
#                     res += 1
#         return res






class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize grid with zeros
        g = [[0] * n for _ in range(m)] # g - 2D grid/matrix
        
        # Mark guards and walls as 2
        for x, y in guards:  # gx, gy -  guard's position 
            g[x][y] = 2    
        for x, y in walls:
            g[x][y] = 2
            
        # Directions: up, right, down, left
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Process each guard's line of sight
        for gx, gy in guards:
            for dx, dy in dirs: # dx, dy - movement direction offsets
                x, y = gx, gy
                while True:
                    x += dx
                    y += dy
                    # Check cells in current direction until hitting boundary or obstacle
                    if x < 0 or x >= m or y < 0 or y >= n or g[x][y] == 2:
                        break
                    g[x][y] = 1
        
        # Count unguarded cells (cells with value 0)
        return sum(row.count(0) for row in g)
        