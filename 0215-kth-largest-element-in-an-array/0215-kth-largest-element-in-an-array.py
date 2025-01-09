class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # # Sorting approach
        # nums.sort()
        # return nums[len(nums) - k]





        # Min Heap approach
        minHeap = []            # create a min heap

        # process the elements using heap
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]  # The root of the heap is the kth largest element





        # # Quickselect approach
        # k = len(nums) - k   # index we are looking for

        # def quickselect(l, r):
        #     pivot, p = nums[r], l
        #     for i in range(l,r):
        #         if nums[i] <= pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p += 1
        #     nums[p], nums[r] = nums[r], nums[p]     # nums[r] = pivot

        #     if p > k:
        #         return quickselect(l, p - 1)
        #     elif p < k:
        #         return quickselect(p + 1, r)
        #     else:   # p = k
        #         return nums[p]

        # return quickselect(0, len(nums) - 1)