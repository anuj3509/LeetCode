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
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res