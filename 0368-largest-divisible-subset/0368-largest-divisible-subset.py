class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # DP solution
        nums.sort()
        dp = [[n] for n in nums]     # dp[i] = longest start at i
        res = []
        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dp[j]
                    dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
            res = dp[i] if len(dp[i]) > len(res) else res
        return res
        


        # # optimized memoization solution
        # nums.sort()
        # cache = {}
        # def dfs(i):
        #     if i == len(nums): return [] 
        #     if i in cache: return cache[i]

        #     res = [nums [i]]
        #     for j in range(i + 1, len(nums)): 
        #         if nums [j] % nums [i] == 0:
        #             tmp = [nums[i]] + dfs(j)
        #             if len(tmp) > len(res):
        #                 res = tmp
        #     cache[i] = res
        #     return res

        # res = []
        # for i in range(len(nums)):
        #     tmp = dfs (i)
        #     if len(tmp) > len(res):
        #         res = tmp
        # return res