class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            # if first is heavier, but here it would be less because we have negated all values in the heap
            if second > first:   
                heapq.heappush(stones, first - second)   # update the weight of the bigger stone
            
        stones.append(0)    # if stones is empty, we will add 0 and then it will be returned
        return abs(stones[0])
