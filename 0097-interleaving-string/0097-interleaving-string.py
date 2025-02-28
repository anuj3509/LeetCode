class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # Bottop-Up dynamic programming approach
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True     # corner value -> out of bounds position in both strings

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
        
        
        
        
        
        # # Recursion with memoisation
        # if len(s1) + len(s2) != len(s3):
        #     return False

        # dp = {}
        # def dfs(i, j, k):
        #     if k == len(s3):
        #         return (i == len(s1)) and (j == len(s2))
        #     if (i, j) in dp:
        #         return dp[(i, j)]
            
        #     res = False
        #     if i < len(s1) and s1[i] == s3[k]:
        #         res = dfs(i + 1, j, k + 1)
        #     if not res and j < len(s2) and s2[j] == s3[k]:
        #         res = dfs(i, j + 1, k + 1)
            
        #     dp[(i, j)] = res
        #     return res
        
        # return dfs(0, 0, 0)
