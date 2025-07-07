class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()   # sort by their start day
        total_days = max(e[1] for e in events)
        res = 0
        heap = []
        i = 0
        n = len(events)
        
        for day in range(1, total_days + 1):
            while i < n and events[i][0] == day:    # add all events that start today
                heapq.heappush(heap, events[i][1])  # push end day
                i += 1

            while heap and heap[0] < day:   # removing all events that have already expired
                heapq.heappop(heap)
                
            if heap:    # attending the event that ends earliest
                heapq.heappop(heap)
                res += 1
        return res