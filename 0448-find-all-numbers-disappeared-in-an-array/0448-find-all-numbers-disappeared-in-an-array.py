class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for num in nums:
            # take the index of this number and mark the number at that index as -ve to indicate visited
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        
        return res