class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # # TC: O(2^n)
        # def dfs(i, total):
        #     if i == len(nums):
        #         return total
        #     return (dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total))    
        #             # include nums[i]               # not include nums[i]

        # return dfs(0, 0)


        # TC: O(n)
        res = 0
        for n in nums:
            res = res | n   # OR operator
        return res * 2**(len(nums) - 1)     # res shifted to left by (len(nums) - 1)