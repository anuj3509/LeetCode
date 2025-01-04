class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l<=r:
            if nums[l] < nums[r]:   # if the sub-array is already sorted
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            
            if nums[m] >= nums[l]:  # checks if the value is a part of the left sorted portion
                # checks if the middle value is greater than the leftmost value, think !! (for only rotated sorted array)
                l = m + 1   # search on the right side of the 'm' pointer
            else:
                r = m - 1   # search on the left side of the 'm' pointer
            res = min(res, nums[m])

        return res