class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # top down memoization 

        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".") # first character matches for that string
            if (j+1) < len(p) and p[j+1] == "*":     #because jth i.e. first character cannot be a '*'
                cache[(i, j)] = (dfs(i, j+2) or  # dont use '*'
                        (match and dfs(i+1, j)))
                return cache[(i, j)]
            
            if match:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)