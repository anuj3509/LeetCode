class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posdiag = set()     # (r+c) is const. [bottom-left to top-right]
        negdiag = set()     # (r-c) is const. [top-left to bottom-right]

        res = 0

        def backtrack(r):       # doing backtracking row by row
            if r == n:      # this means that we found a valid board
                nonlocal res
                res += 1
                return
            
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue

                # if not in any set, place the queen at this place
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)

                backtrack(r + 1)

                # if it pops out of backtracking, we undo everything for next iteration of loop
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)

        backtrack(0)
        return res