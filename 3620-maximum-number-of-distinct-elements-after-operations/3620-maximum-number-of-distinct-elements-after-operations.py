class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        lower = float("-inf")

        for num in nums:
            currLower = max(lower + 1, num - k)
            if currLower <= num + k:
                res += 1
                lower = currLower

        return res