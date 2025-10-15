class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        best = 0
        streaks = []
        count = 0
        last = -float("inf")

        for x in nums:
            if x > last:
                count += 1
            else:
                count = 1
            last = x
            streaks.append(count)

        # one long streak
        best = max(streaks) // 2

        # end of a strak, and then beginning of a another
        for i in range(len(streaks)):
            if streaks[i] <= best:
                continue
            if i - streaks[i] < 0:
                continue
            
            if streaks[i - streaks[i]] >= streaks[i]:
                best = max(best, streaks[i])
        
        return best
                