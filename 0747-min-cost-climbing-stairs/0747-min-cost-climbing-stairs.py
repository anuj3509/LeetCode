class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10, 15, 20] 0    :   0 is the index for top floor

        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            # cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i + 2])
            # the above line can be written as follows to reduce operations
            cost[i] += min(cost[i+1], cost[i + 2])
        
        return min(cost[0], cost[1])
