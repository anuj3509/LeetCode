class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}

        for n in nums:
            countmap[n] = 1 + countmap.get(n,0) #create a hashmap for the input array

        arr = []
        for n,count in countmap.items():
            arr.append([count,n])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        
        return result