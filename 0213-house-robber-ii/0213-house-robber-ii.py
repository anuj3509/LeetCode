class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        # nums[0] is for the case when our input array has only one house

    def helper(self, nums):
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n+1, n+2, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2