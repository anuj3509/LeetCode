class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        # left pointer is buy and right is sell
        maxprofit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:   #check for profit
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit)
            else:
                l = r   #if no profit, then at the time we reach this
                # condition {condition: prices[l] < prices[r]}, 
                # we will have our right pointer at the lowest value in 
                # the array
            r += 1

        return maxprofit