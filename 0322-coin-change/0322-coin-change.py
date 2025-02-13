class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # TC -> O(amount * len(coins)) ; SC -> O(amount)
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0   # means if we want to compute amount 0, it only takes 0 coins

        for a in range(1, amount + 1):
            for c in coins:
                if (a - c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])     # 1 is to increment coins used by 1

        return dp[amount] if dp[amount] != (amount + 1) else -1     
        # amount + 1 is the starting value which we initialised with