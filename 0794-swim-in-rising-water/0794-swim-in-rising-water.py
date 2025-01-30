class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minheap = [[grid[0][0], 0, 0]]  # (time/maxHeight, row, col)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]        
        
        visit.add((0, 0))
        while minheap:
            t, r, c = heapq.heappop(minheap) 
            if r == n - 1 and c == n - 1:
                return t 

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == n or neiC == n or
                    (neiR, neiC) in visit):
                    continue 
                visit.add((neiR, neiC))
                heapq.heappush(minheap, [max(t, grid[neiR][neiC]), neiR, neiC]) 

            # we do not need a return statement because it is guarenteed that 
            # we will reach a solution/destination     