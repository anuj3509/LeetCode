class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):     # i is the index of value that we are making a decision on
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include nums[i]
            subset.pop()    # pop the element we just appended above
            dfs(i + 1)      # so this recusrsive call will have an empty subset passed to it

        dfs(0)
        return res