class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:  
                continue
            # i>0 indicates that we are checking the next 
            # value and val == nums[i-1] checks if the current value is same as previous 
            # value. We only check the previous value bcoz we have sorted the array and if 
            # duplicates existed, they would be adjacent to each other
            
            l,r = i+1, len(nums)-1
            while l < r:
                threesum = val + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res