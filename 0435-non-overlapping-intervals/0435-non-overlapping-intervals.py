class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]   # end value of the first interval

        # start iterating through the second interval onwards
        for start, end in intervals[1:]:
            # not overlappipng case
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)     # we will keep the intevals which end earlier
        return res