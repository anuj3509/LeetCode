class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 1. check all remainders
        for row in grid:
            for n in row:
                if n % x != grid[0][0] % x:
                    return False

        # 2. flatten and sort the input
        nums = sorted([n for row in grid for n in row])

        # 3. prefix / suffix sum solution
        prefix = 0
        total = sum(nums)
        res = float("inf")

        for i in range(len(nums)):
            cost_left = nums[i] * i - prefix
            cost_right = total - prefix - (nums[i] * (len(nums) - i))
            operations = (cost_left + cost_right) // x
            res=min(res, operations)
            prefix += nums[i]
        return res