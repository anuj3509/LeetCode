class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]        
        
        # effort matrix initialized to infinity in all values
        effort = [[float('inf')] * col for _ in range(row)]
        effort[0][0] = 0

        minheap = [(0, 0, 0)]  # (current effort, row, col)
        while minheap:
            curr_effort, r, c = heappop(minheap)
            if r == row - 1 and c == col - 1:
                return curr_effort      # return current(minimum) effort if we reach bottom right cell

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if 0 <= neiR < row and 0 <= neiC < col:
                    new_effort = max(curr_effort, abs(heights[neiR][neiC] - heights[r][c]))

                    # update and push into minheap if found a better path
                    if new_effort < effort[neiR][neiC]:
                        effort[neiR][neiC] = new_effort
                        heappush(minheap, (new_effort, neiR, neiC))