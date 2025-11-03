class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0     # total time
        l = 0

        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:   # eliminating the left balloon
                    res += neededTime[l]
                    l = r
                else:       # eliminating the left balloon
                    res += neededTime[r]
            else:
                l = r
        return res