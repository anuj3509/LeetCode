class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        # Bottom-Up approach with optimised memory
        dp = defaultdict(int)
        dp[0] = 1    # current sum is 0 -> 1 way to have that
        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for curr_sum, count in dp.items():
                next_dp[curr_sum + nums[i]] += count
                next_dp[curr_sum - nums[i]] += count
                dp = next_dp
        return dp[target]

        
        
        
        # # Bottom-Up approach
        # dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        # dp[0][0] = 1    # 0 elements available, current sum is 0, 1 way to have that
        # for i in range(len(nums)):
        #     for curr_sum, count in dp[i].items():
        #         dp[i + 1][curr_sum + nums[i]] += count
        #         dp[i + 1][curr_sum - nums[i]] += count
        # return dp[len(nums)][target]
        
        
        
        # # Top-Down approach with memoization

        # dp = {}     # (index, curr_sum) 
        # def backtrack(i, curr_sum):
        #     if (i, curr_sum) in dp:
        #         return dp[(i, curr_sum)]
        #     if i == len(nums):      # if i is at the end of the array
        #         return 1 if curr_sum == target else 0

        #     dp[(i, curr_sum)] = (
        #         backtrack(i + 1, curr_sum + nums[i]) + 
        #         backtrack(i + 1, curr_sum - nums[i])
        #     )
        #     return dp[(i, curr_sum)]
        # return backtrack(0, 0)