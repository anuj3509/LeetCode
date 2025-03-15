class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def isvalid(capability):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= capability:
                    i += 2
                    count += 1
                else:
                    i += 1
                if count == k:
                    break
            return count == k


        # Binary Search idea came from question - koko eating bananas
        # Search space: [min(nums), max(nums)]
        l, r = min(nums), max(nums)
        while l <= r:
            m = (l + r) // 2
            if isvalid(m):
                res = m
                r = m - 1   # we try a smaller capability
            else:
                l = m + 1   # we try a bigger capability
        return res