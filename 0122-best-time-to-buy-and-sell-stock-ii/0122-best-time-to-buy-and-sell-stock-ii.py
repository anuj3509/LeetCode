class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):     # we skip 0 because we. know zero does not have a previous value
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit