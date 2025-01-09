class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # each task takes 1 unit time, minimize idle time
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()     # pair of [-cnt, idle time]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:   # if time has been reached
                heapq.heappush(maxHeap, q.popleft()[0])

        return time