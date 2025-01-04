class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l<=r:
            # if nums[l] < nums[r]:   # if the sub-array is already sorted
            #     res = min(res, nums[l])
            #     break

            m = (l + r) // 2
            
            if nums[m] > nums[r]:  
                l = m + 1   # search on the right side of the 'm' pointer
            elif nums[m] < nums[r]:
                r = m   # search on the left side of the 'm' pointer
            else:   # nums[m] == nums[r] --> indicating duplicate
                r -= 1
            res = min(res, nums[m])
        return res