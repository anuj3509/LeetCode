class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # # Memoization Solution [TC = SC = O(m * n)]
        # cache = {}
        # def dfs(i, a):
        #     if a == amount:
        #         return 1
        #     if a > amount:
        #         return 0
        #     if i == len(coins):
        #         return 0
        #     if (i, a) in cache:
        #         return cache[(i, a)]

        #     cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
        #     return cache[(i, a)]

        # return dfs(0, 0)




        # 2D DP cache -> TC = O(m * n); SC = O(n) ->  Suboptimal solution - memory optimized
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]