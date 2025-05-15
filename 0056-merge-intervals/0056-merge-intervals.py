class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i : i[0])   # sort intervals by their start value
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastend = output[-1][1]     # end value of most recently added interval

            if start <= lastend:
                output[-1][1] = max(lastend, end)
            else:
                output.append([start, end])
        return output