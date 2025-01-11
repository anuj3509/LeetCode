class MedianFinder:

    def __init__(self):
        # we will have two heaps: large (right half of the final array: minheap) and 
        # small (left half of the final array: maxheap). Heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure that in every num in small <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # checking for uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
         

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):   # if small (maxheap) is longer in size
            return -1 * self.small[0]
        elif len(self.large) > len(self.small): # if large (minheap) is longer in size
            return self.large[0]
        else:   # if both heap are of same size
            return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()