class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # initialize the entire 2D grid as 0 
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # find max of the right and the bottom value. we are not adding 1 because the characters did not match each other
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]

        # TC = SC: O(n * m)