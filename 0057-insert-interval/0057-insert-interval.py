class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):

            # new interval has an end value smaller than the start value of the first interval
            if newInterval[1] < intervals[i][0]:     
                res.append(newInterval)
                return res + intervals[i:]  

            # new interval goes after the current interval we are at right now
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            # new interval is overlapping with the curent interval we are at
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)

        return res