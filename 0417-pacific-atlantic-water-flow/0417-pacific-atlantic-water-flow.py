class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:  
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevheight):
            if ((r, c) in visit or
                r < 0 or c < 0 or r == rows or c == cols or 
                heights[r][c] < prevheight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        for c in range(cols):
            # first row is going to pacific ocean
            dfs(0, c, pacific, heights[0][c])   # prevheight = heights[r][c]
            # last row is going to atlantic ocean
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            # first column is going to pacific ocean
            dfs(r, 0, pacific, heights[r][0])   # prevheight = heights[r][c]
            # last column is going to atlantic ocean
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res