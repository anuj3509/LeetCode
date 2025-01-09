class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # # Sorting approach
        # nums.sort()
        # return nums[len(nums) - k]


        # Min Heap approach
        minHeap = []            # create a min heap

        # process the remaining elements
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]  # The root of the heap is the kth largest element
