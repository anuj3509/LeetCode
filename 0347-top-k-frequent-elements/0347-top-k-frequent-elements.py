class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # countmap = {}
        # for n in nums:
        #     countmap[n] = 1 + countmap.get(n,0) #create a hashmap for the input array

        # arr = []
        # for n,count in countmap.items():
        #     arr.append([count,n])
        # arr.sort()

        # result = []
        # while len(result) < k:
        #     result.append(arr.pop()[1])

        # return result


        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for num in count.keys():
            # append values to a minHeap to store.  if the size exceeds k, pop the element
            # from the heap. this will pop the element with the least frequency
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            # pop the value from the heap and append its value to the result
            # note that the value is stored at index 1 and index 0 is frequency
            res.append(heapq.heappop(heap)[1])
        
        return res