class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # TC: O(n * m * 4^len(word)) = O(n * m * 4^n)
        
        rows, cols = len(board), len(board[0])
        path = set()    # to add all current val/position in path so that we dont revisit them

        def dfs(r, c, i):   
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or   # out of bounds condition
                word[i] != board[r][c] or   # if we found the wrong character
                (r, c) in path):            # if we are visiting the same position twice
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res


        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False