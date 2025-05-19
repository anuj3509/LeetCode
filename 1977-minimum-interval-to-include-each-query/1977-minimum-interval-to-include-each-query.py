class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minheap = []
        res, i = {}, 0  # result is a hashmap because we want the relative order of queries before sorting

        for q in sorted(queries):
            # add values in the minheap
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minheap, (r - l + 1, r))
                i += 1
            
            # continue to pop from the minheap
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)  # popping the invalid intervals which are too far to the left
            res[q] = minheap[0][0] if minheap else -1
        return [ res[q] for q in queries ]