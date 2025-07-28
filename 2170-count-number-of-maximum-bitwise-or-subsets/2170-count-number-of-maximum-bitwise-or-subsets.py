class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num  # overall max OR

        res = 0

        def dfs(i, cur_or):
            nonlocal res
            if i == len(nums):
                if cur_or == max_or:
                    res += 1
                return
            
            dfs(i + 1, cur_or | nums[i])    # including nums[i]
            dfs(i + 1, cur_or)              # excluding nums[i]

        dfs(0, 0)
        return res

        # TC: O(2^n)