class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        last_min = last_max = last_bad = -1
        for i, v in enumerate(nums):
            # if out of [minK, maxK], reset window
            if v < minK or v > maxK:
                last_bad = i
            # update last positions of minK and maxK
            if v == minK:
                last_min = i
            if v == maxK:
                last_max = i
            # any subarray ending here must start after last_bad
            # and must include both a minK and a maxK
            res += max(0, min(last_min, last_max) - last_bad)
        return res
