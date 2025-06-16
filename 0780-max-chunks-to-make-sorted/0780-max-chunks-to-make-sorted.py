class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        currentMax = -1
        res = 0     # count of sorted chunks - partitions

        for i, n in enumerate(arr):
            currentMax = max(n, currentMax)
            if currentMax == i:
                res += 1
        return res