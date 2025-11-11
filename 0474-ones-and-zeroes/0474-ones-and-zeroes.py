class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
       
        # # Top Down DP with memoization
        # dp = {}

        # def dfs(i, m, n):
        #     if i == len(strs):
        #         return 0
            
        #     if (i, m, n) in dp:
        #         return dp[(i, m, n)]
            
        #     m_count, n_count = strs[i].count('0'), strs[i].count('1')
        #     dp[(i, m, n)] = dfs(i+1, m, n)
        #     if m_count <= m and n_count <= n:
        #         dp[(i, m, n)] = max(
        #             dfs(i+1, m, n),  # not include the string at index 'i'
        #             1 + dfs(i+1, m - m_count, n - n_count)  # include the string at index 'i'
        #         )
        #     return dp[(i, m, n)]

        # return dfs(0, m, n)



        # Iterative Dynamic Programming
        dp = defaultdict(int)

        for i in range(len(strs)):
            s = strs[i]
            m_count, n_count = strs[i].count('0'), strs[i].count('1')
            for m in range(0, m + 1):
                for n in range(0, n + 1):
                    if m_count <= m and n_count <= n:
                        dp[(i, m, n)] = max(
                            1 + dp[(i-1, m - m_count, n - n_count)],  # include the string at index 'i'
                            dp[(i-1, m, n)]  # not include the string at index 'i'
                        )
                    else:
                        dp[(i, m, n)] = dp[(i - 1, m, n)]
        
        return dp[(len(strs) - 1, m, n)]
