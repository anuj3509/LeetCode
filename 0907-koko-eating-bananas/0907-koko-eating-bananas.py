class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        res = r 
        # instead of 0, we set the result to be the max value from the piles,
        # because we know that this is definitely going to work
    
        while l <= r:
            k = (l + r) // 2    # middle point for the binary search
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res



# --------------------Junk Approach (Not working)------------------------------
        # k = (l + r) // 2    # middle point for the binary search
        # total = 0
        # for i in piles:
        #     # piles(i) = piles(i) // k
        #     total += i // k
        # sumarray = []

        # if total <= h:
        #     sumarray.append(total)

        # return min(sumarray)
# -----------------------------------------------------------------------------
