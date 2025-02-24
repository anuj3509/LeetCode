class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or selling
        # If buy -> i + 1
        # If sell -> i + 2

        dp = {}     # key = (i, buying) ; val = max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Case: Buying
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            # Case: Selling
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)     # initial buying state is True because we will always buy on day 1