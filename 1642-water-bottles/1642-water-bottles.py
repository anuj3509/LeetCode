class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = 0
        empty = 0
        while numBottles > 0:
            drank += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty %= numExchange
        return drank

        # TC: O(log_m(n)) ; m: numBottles, n: numExchange

        
        # return numBottles + (numBottles-1)//(numExchange-1)