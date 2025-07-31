class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l, r = 0, 1
        res = -1
        
        while r < len(nums):
            if nums[l] < nums[r]:
                diff = nums[r] - nums[l]
                res = max(res, diff)  
            else:
                l = r
            r += 1
        return res    

        # TC: O(n)    ;   SC: O(1)
        # Similar to - best time to buy & sell stock  