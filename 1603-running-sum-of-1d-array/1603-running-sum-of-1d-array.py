class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:        
        for i in range(1, len(nums)):
            # modifying the input array to store the runnig sum instead of occupying new memory
            nums[i] += nums[i-1]    
        return nums