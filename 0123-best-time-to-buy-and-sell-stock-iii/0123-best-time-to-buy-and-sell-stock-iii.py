class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        
        dp = [0 for i in range(len(prices))]

        for t in range(1, 2+1):
            pos = -prices[0]
            profit = 0
            for i in range(1, len(prices)):
                pos = max(pos, dp[i]-prices[i])
                profit = max(profit, pos + prices[i])
                dp[i] = profit
        return profit
