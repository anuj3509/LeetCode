class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set()     # (r+c) is const. [bottom-left to top-right]
        negdiag = set()     # (r-c) is const. [top-left to bottom-right]

        res = []
        board = [["."]*n for i in range(n)]     # n x n empty board

        def backtrack(r):       # doing backtracking row by row
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                
                # if not in any set, place the queen at this place
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # if it pops out of backtracking, we undo everything for next iteration of loop
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        return res