class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)   # base case of 0 since we know that the total sum can be 0 when we dont choose any elements
        target = sum(nums) / 2
        
        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False